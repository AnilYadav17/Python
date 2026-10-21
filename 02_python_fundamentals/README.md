# 🐍 02_Python_Fundamentals: Core Syntax & Logic

## Overview
Python Fundamentals forms the bedrock of everything you will build in programming. This section covers how Python stores data in memory (variables and data types), transforms values (type casting and operators), makes decisions (branching conditionals and match-case), and repeats actions (loops, ranges, and loop-control statements).

Whether you are calculating mathematical models or filtering logs, these fundamental building blocks are executed in every single Python application.

---

## Learning Objectives
By studying this module, you will understand:
1. Dynamic typing, variable assignment, and Python's primitive data types (`int`, `float`, `bool`, `str`, `complex`, `None`).
2. Type casting rules (implicit vs. explicit casting) and variable memory inspection (`id()`, `sys.getsizeof()`).
3. Arithmetic, relational, logical, assignment, bitwise (`<<`, `>>`, `&`, `|`, `^`, `~`), identity (`is`, `is not`), and membership (`in`, `not in`) operators.
4. Decision trees using `if`, `if-else`, `elif`, nested conditions, and modern `match-case` pattern matching.
5. Iteration mechanics using `for` loops, `while` loops, the `range()` generator, `break`, `continue`, and Python's unique `for-else` / `while-else` construct.
6. Number theory algorithms: Armstrong numbers, palindromes, factorials, reverse digits, and prime checking.

---

## Prerequisites
* Completion of **[01_getting_started](../01_getting_started/)** (Python installed and terminal execution understood).

---

## Learning Path

```text
1. Data Types & Variables (Day 4 - 5)
   └── Numbers, Strings, Booleans, None, Size & ID
       ▼
2. Operators & Precedence (Day 6 - 7, Day 13)
   └── Arithmetic, Logical, Comparison, Bitwise, Identity & Membership
       ▼
3. Conditional Branching (Day 7 - 8, 6May)
   └── if, if-else, elif, Nested Conditions, Match-Case
       ▼
4. Loops & Iterations (Day 9, Day 11, Day 12)
   └── while, for, range(), break, continue, loop-else
       ▼
5. Number Algorithms & Pattern Programming (Day 10, 8May)
   └── Armstrong, Palindrome, Factorial, Prime, Star/Number Patterns
```

---

## Repository Contents & Examples

All classroom programs and lecture examples are located in **`Class_Work/`**:

| Topic Area | Directory / Location | Key Programs Covered |
|:---|:---|:---|
| **Data Types & Memory** | `Class_Work/Day4`, `Day5` | `bool.py`, `type_casting.py`, `complex_type.py`, `size_id.py`, `none.py`, `presedence.py` |
| **Operators & Expressions** | `Class_Work/Day6`, `Day7`, `Day13` | `Arith1.py`, `logical.py`, `rela1.py`, `bitwise/` (`left_shift.py`, `swap_xor.py`), `is/`, `in/` |
| **Branching & Conditionals** | `Class_Work/Day7/if`, `Day8/`, `6May/` | `if_else/`, `elif/`, `nested_if_else/`, `matchcase/`, `guard_case/` |
| **Loops & Iteration** | `Class_Work/Day9/loops/` | `while/` (counters, sums), `for/` (traversal), `range/` (start, stop, step) |
| **Loop Control & Else** | `Class_Work/Day11/`, `Day12/` | `Break/` (`prime.py`, `choice.py`), `Continue/`, `for_else/`, `while_else/` |
| **Algorithmic Numbers** | `Class_Work/Day10/loops/` | `armstrong.py`, `fact.py`, `pallindrome.py`, `perfect_for.py`, `reverse.py` |
| **Pattern Programming** | `Class_Work/8May/pattern/` | Pyramid and coordinate grid patterns |
| **Exam Revision Guide** | Root of this folder | **[exam_preparation_guide.md](./exam_preparation_guide.md)** & **[PDF](./exam_preparation_guide.pdf)** |

---

## How to Run Examples

Navigate to any subfolder and run with Python 3:

```bash
# Example 1: Testing bitwise XOR swap
python3 Class_Work/Day13/bitwise/swap_xor.py

# Example 2: Testing Armstrong number checker
python3 Class_Work/Day10/loops/armstrong.py

# Example 3: Testing match-case
python3 Class_Work/6May/matchcase/1.py
```

---

## Practice & Assignments

Ready to practice? Solve the extensive topic-wise assignment collections in **`09_practice_and_assignments/01_Basics/`**:
* **[01_Input_Output](../09_practice_and_assignments/01_Basics/01_Input_Output/)** — Console I/O formatting.
* **[02_Conditions_and_Branching](../09_practice_and_assignments/01_Basics/02_Conditions_and_Branching/)** — Decision making challenges.
* **[03_Calculations_and_Operators](../09_practice_and_assignments/01_Basics/03_Calculations_and_Operators/)** — Math formulas, electricity billing, discounts.
* **[04_Loops_and_Numbers](../09_practice_and_assignments/01_Basics/04_Loops_and_Numbers/)** — Multiplications, primes, step differences.
* **[05_Pattern_Programming](../09_practice_and_assignments/01_Basics/05_Pattern_Programming/)** — 90+ technical pattern challenges.

---

## Common Beginner Mistakes

1. **Confusing `==` with `is`:**
   * `==` tests for equality of **values** (`[1, 2] == [1, 2]` is `True`).
   * `is` tests for **identity** / same memory address (`[1, 2] is [1, 2]` is `False`).
2. **Off-by-One in `range(start, stop)`:**
   * In Python, `range(1, 10)` generates numbers from `1` up to `9`, NOT `10`. The `stop` parameter is exclusive.
3. **Misunderstanding `for-else` / `while-else`:**
   * The `else` block on a loop executes **only if the loop finishes without hitting a `break` statement**.
4. **Modifying loop variables inside a `for` loop:**
   * In Python `for i in range(5): i += 2` does not skip iterations; `i` is rebound by the iterator on each step.

---

## Next Step

👉 Advance to **[03_python_collections](../03_python_collections/)** to master Lists, Dictionaries, Sets, Tuples, and 2D Matrices!
