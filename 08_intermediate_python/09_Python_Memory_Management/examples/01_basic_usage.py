"""
01_basic_usage.py
Demonstrates core memory management principles:
- Reference counting with sys.getrefcount()
- Object identity with id() and 'is'
- Value equality with '=='
- String interning using sys.intern()
"""

import sys

def demonstrate_ref_counting():
    print("--- 1. Reference Counting with sys.getrefcount() ---")
    # Allocate a new list object
    data = [1, 2, 3]

    # Note: sys.getrefcount() creates a temporary local reference, so it returns 1 + active_refs
    print(f"Initial ref count of 'data': {sys.getrefcount(data) - 1}")  # 1

    alias1 = data
    print(f"After 'alias1 = data':      {sys.getrefcount(data) - 1}")  # 2

    alias2 = data
    print(f"After 'alias2 = data':      {sys.getrefcount(data) - 1}")  # 3

    del alias1
    print(f"After 'del alias1':          {sys.getrefcount(data) - 1}")  # 2

    del alias2
    print(f"After 'del alias2':          {sys.getrefcount(data) - 1}")  # 1


def demonstrate_identity_vs_equality():
    print("\n--- 2. Object Identity (id, is) vs Equality (==) ---")
    list_a = [10, 20, 30]
    list_b = [10, 20, 30]

    print(f"list_a == list_b (Values):    {list_a == list_b}")  # True
    print(f"list_a is list_b (Addresses): {list_a is list_b}")  # False
    print(f"Address of list_a: {hex(id(list_a))}")
    print(f"Address of list_b: {hex(id(list_b))}")


def demonstrate_string_interning():
    print("\n--- 3. String Interning with sys.intern() ---")
    # Dynamically constructed strings are not interned by default
    str1 = "".join(["hello", "_", "world"])
    str2 = "".join(["hello", "_", "world"])

    print(f"Before interning -> str1 is str2: {str1 is str2}")  # False

    # Force interning into CPython's global string table
    interned_1 = sys.intern(str1)
    interned_2 = sys.intern(str2)

    print(f"After interning  -> interned_1 is interned_2: {interned_1 is interned_2}")  # True
    print("Benefit: Interned strings can be compared via fast pointer identity O(1)!")


def main():
    demonstrate_ref_counting()
    demonstrate_identity_vs_equality()
    demonstrate_string_interning()

if __name__ == "__main__":
    main()
