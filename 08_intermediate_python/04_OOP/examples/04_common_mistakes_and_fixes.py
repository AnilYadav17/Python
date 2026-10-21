"""
04_common_mistakes_and_fixes.py
Demonstrates common OOP architectural antipatterns and fixes:
1. Misguided inheritance (subclassing list to make a Stack) vs Composition
2. Broken super() cooperative multiple inheritance (The Diamond Problem)
"""

def mistake_1_inheritance_vs_composition():
    print("--- 1. Inheritance vs Composition for Stack ---")

    # BAD: Inheriting from list exposes all list mutation methods (insert, sort, pop(0))
    # which violates the LIFO encapsulation contract of a Stack!
    class StackBuggy(list):
        def push(self, item):
            self.append(item)

    bad_stack = StackBuggy()
    bad_stack.push(10)
    bad_stack.push(20)
    # User can inadvertently break the stack:
    bad_stack.insert(0, 999)  # Breaks LIFO!
    print(f"Buggy Stack exposes insert: {bad_stack}")

    # FIX: Use COMPOSITION with private internal container
    class StackClean:
        def __init__(self):
            self._storage = []  # Private backing list

        def push(self, item):
            self._storage.append(item)

        def pop(self):
            if not self._storage:
                raise IndexError("pop from empty stack")
            return self._storage.pop()

        def peek(self):
            return self._storage[-1] if self._storage else None

        def __len__(self):
            return len(self._storage)

        def __repr__(self):
            return f"StackClean({self._storage})"

    clean_stack = StackClean()
    clean_stack.push(10)
    clean_stack.push(20)
    print(f"Clean Stack: {clean_stack}, Peek: {clean_stack.peek()}, Popped: {clean_stack.pop()}")


def mistake_2_diamond_problem_and_super():
    print("\n--- 2. Diamond Problem and super() Cooperative MRO ---")

    # Diamond hierarchy:
    #       A
    #      / \
    #     B   C
    #      \ /
    #       D

    class A:
        def action(self):
            print("  A.action()")

    class B(A):
        def action(self):
            print("  B.action() executing...")
            super().action()

    class C(A):
        def action(self):
            print("  C.action() executing...")
            super().action()

    class D(B, C):
        def action(self):
            print("  D.action() executing...")
            super().action()

    print("Class D Method Resolution Order (MRO):")
    for idx, cls in enumerate(D.mro(), 1):
        print(f"  {idx}. {cls.__name__}")

    print("\nInvoking D().action():")
    d_instance = D()
    d_instance.action()
    print("Notice: A.action() runs exactly ONCE because super() traverses the MRO cooperatively!")


def main():
    mistake_1_inheritance_vs_composition()
    mistake_2_diamond_problem_and_super()

if __name__ == "__main__":
    main()
