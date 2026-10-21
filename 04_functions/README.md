# ⚡ 04_Functions: Functional Programming, Scopes & Decorators

## Overview
Functions are the fundamental units of code reusability, abstraction, and modularity in Python. Rather than repeating code across scripts, functions bundle logic into parameterized blocks that accept arguments and return computed results.

Python treats functions as **first-class citizens**—functions can be assigned to variables, passed as arguments to other functions, returned from functions, and nested inside one another. This unlocks powerful functional programming paradigms including closures, decorators, recursion, lambdas, and higher-order functions (`map`, `filter`).

---

## Learning Objectives
By studying this module, you will understand:
1. Function definitions (`def`), positional vs. keyword parameters, and default values.
2. Value returns (`return` vs. `None`) and multi-value tuple returns.
3. Variable scope resolution governed by the **LEGB Rule** (Local, Enclosing, Global, Built-in).
4. Anonymous functions (`lambda`) for concise inline operations.
5. Higher-order transformations using `map()` and `filter()`.
6. Recursive thinking: Establishing the base case and recursive relation (factorials, digit count, powers).
7. Closures and Decorator functions (`@decorator_syntax`) to enhance existing functions without modifying their source code.

---

## Prerequisites
* **[02_python_fundamentals](../02_python_fundamentals/)** (Variables, loops, conditionals)
* **[03_python_collections](../03_python_collections/)** (Lists and strings for mapping/filtering)

---

## Learning Path

```text
1. Function Fundamentals (12Jun, 15Jun)
   └── def, Parameters, Positional & Default Arguments, Return Statements
       ▼
2. Lambda Expressions (17Jun_Lambda)
   └── Anonymous Functions, Inline Conditionals
       ▼
3. Map & Filter Higher-Order Functions (18Jun_Filter)
   └── Transforming Sequences, Filtering Truthy Values, Type Conversion
       ▼
4. Recursion (22Jun_Recursion)
   └── Base Cases, Call Stack, Factorials, Power Calculation, Digit Counting
       ▼
5. Decorators & Closures (24Jun_Decorators)
   └── Wrapper Functions, First-Class Functions, Metaprogramming
```

---

## Repository Contents & Examples

All lecture programs are organized in **`Class_Work/`**:

| Subfolder | Concept | Key Files & Descriptions |
|:---|:---|:---|
| 📁 **`Class_Work/12Jun`** | Declarations & Returns | `1.py` (definition order), `2.py`, `3.py` (dynamic add), `4.py`, `5.py`, `return1.py` |
| 📁 **`Class_Work/15Jun`** | Default Args & Modules | `1.py` (default salaries), `2.py`, `calci.py` (calculator function suite) |
| 📁 **`Class_Work/17Jun_Lambda`** | Anonymous Functions | `conditional_logic.py` (max of two via lambda), `square_add.py` |
| 📁 **`Class_Work/18Jun_Filter`** | Map & Filter | `map_and_filter.py`, `remove_empty.py` (cleaning strings), `string_to_int.py` |
| 📁 **`Class_Work/22Jun_Recursion`** | Recursive Algorithms | `power.py` ($x^n$), `digits_Count.py`, `Recursion/1.py` (factorial), `2.py` (sum), `3.py` (countdown) |
| 📁 **`Class_Work/24Jun_Decorators`** | Function Wrapping | `1.py` (decorator implementation wrapping execution) |
| 📁 **`Demo/`** | Scratchpad | `1.py` - `4.py`, `test.py` (sandbox function experiments) |

---

## How to Run Examples

```bash
# Test the calculator functions:
python3 04_functions/Class_Work/15Jun/calci.py

# Test filter removing empty strings:
python3 04_functions/Class_Work/18Jun_Filter/remove_empty.py

# Test recursive factorial and countdown:
python3 04_functions/Class_Work/22Jun_Recursion/Recursion/1.py
```

---

## Practice & Assignments

Solve the functions assignments in **`09_practice_and_assignments/02_Functions/`**:
* **[01_Basics_and_Lambda](../09_practice_and_assignments/02_Functions/01_Basics_and_Lambda/)** — Parameter passing, lambda transforms.
* **[02_Recursion_and_Arguments](../09_practice_and_assignments/02_Functions/02_Recursion_and_Arguments/)** — Base cases, nested calls.
* **[03_Recursion_Advanced](../09_practice_and_assignments/02_Functions/03_Recursion_Advanced/)** — Fibonacci, string reversal, tower problems.
* **[04_Decorators](../09_practice_and_assignments/02_Functions/04_Decorators/)** — Logging decorators, timer decorators, validation wrappers.

---

## Common Beginner Mistakes

1. **Forgetting to Return a Value:**
   * In Python, any function that ends without an explicit `return` statement returns `None` by default. Assigning `x = print_sum(a, b)` stores `None` in `x`.
2. **Exceeding Maximum Recursion Depth:**
   * A recursive function without a base case will recurse indefinitely until Python triggers `RecursionError: maximum recursion depth exceeded`.
3. **Modifying Global Variables Without the `global` Keyword:**
   * Reading a global variable works, but assigning to it inside a function creates a new local variable unless declared with `global var_name`.
4. **Expecting `map()` or `filter()` to Return a List:**
   * In Python 3, `map()` and `filter()` return lazy iterators! You must cast them via `list(map(...))` to view or index the results.

---

## Next Step

👉 Advance to **[05_object_oriented_programming](../05_object_oriented_programming/)** to master Classes, Objects, Inheritance, Polymorphism, Encapsulation, and Abstraction!
