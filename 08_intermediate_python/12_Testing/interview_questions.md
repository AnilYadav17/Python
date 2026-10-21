# 12. Testing — Interview & Viva Questions

---

### Q1: What is the Golden Rule of patching with `unittest.mock.patch`?
**Model Answer:**
- **"Patch where an object is looked up, NOT where it is defined."**
- If module `app.py` contains `from database import query`, the name `query` has already been bound into `app`'s local module namespace.
- Patching `@patch('database.query')` will modify the original module, but `app.py` will continue executing its pre-imported local reference.
- You must patch the lookup location: `@patch('app.query')`.

---

### Q2: How does `pytest` implement assertion introspection without requiring special assertion methods like `assertEqual`?
**Model Answer:**
- `pytest` uses **AST (Abstract Syntax Tree) assertion rewriting**.
- During test discovery and import via `sys.meta_path`, pytest intercepts the Python bytecode compilation of test files.
- It parses the syntax tree of standard `assert a == b` statements and rewrites them to record and display the evaluated runtime values of every sub-expression, comparison operand, and container element.
- When an assertion fails, pytest prints a rich diagnostic diff showing intermediate values, eliminating the need for `self.assertEqual(a, b)`.

---

### Q3: What is the difference between a `Mock` and a `MagicMock` in Python?
**Model Answer:**
- `Mock` is the base test double object that records calls, arguments, and return values for arbitrary attributes and methods.
- `MagicMock` is a subclass of `Mock` that comes pre-configured with default mock implementations for all Python **magic/dunder methods** (e.g. `__len__`, `__iter__`, `__enter__`, `__exit__`, `__getitem__`, `__str__`).
- You should use `MagicMock` whenever the mocked object needs to participate in Python language protocols, such as context managers (`with mock:`), iterables (`for x in mock:`), or collections (`len(mock)`).

---

### Q4: Why is using `create_autospec=True` recommended when creating mocks?
**Model Answer:**
- By default, `Mock` and `MagicMock` dynamically create any attribute or method accessed on them.
- If a developer accidentally misspells an assertion (e.g. writing `mock.assert_called_once_with()` as `mock.assert_called_once_wit()`), the mock dynamically creates the misspelled attribute without raising an error, causing the test to **pass silently while asserting nothing**.
- Furthermore, standard mocks allow calling non-existent methods on the mocked class.
- `create_autospec=True` inspects the real class signature, enforcing that only actual methods exist on the mock and validating that arguments passed during calls match the real signature, raising `AttributeError` or `TypeError` on mismatches.

---

### Q5: Explain the fixture lifecycle in `pytest` and how teardown logic is implemented.
**Model Answer:**
- A fixture defines a reusable test dependency using `@pytest.fixture`.
- The fixture lifecycle consists of setup, test execution, and teardown:
  - Code before `yield` executes prior to the test (Setup).
  - The value yielded is injected into the test function's arguments.
  - The test runs.
  - Code after `yield` executes immediately after the test completes, regardless of whether the test passed or failed (Teardown/Cleanup).
- Fixtures can be scoped: `function` (default), `class`, `module`, or `session`.

---

### Q6: What is the difference between Mocks, Stubs, and Fakes?
**Model Answer:**
- **Stub**: An object that provides pre-canned, hardcoded responses to method calls made during the test (state verification).
- **Mock**: An object pre-programmed with expectations about which calls it should receive, verifying interactions and behavior (behavior verification).
- **Fake**: A lightweight, fully working implementation of an external dependency that takes operational shortcuts unsuitable for production (e.g. using an in-memory dictionary or SQLite instead of an external DynamoDB or PostgreSQL cluster).

---

### Q7: What is Test-Driven Development (TDD), and what are its primary engineering benefits?
**Model Answer:**
- TDD is an iterative development discipline following the **Red-Green-Refactor** cycle:
  1. Write a failing unit test that defines a small requirement (Red).
  2. Implement the simplest code possible to pass the test (Green).
  3. Refactor the code for design clarity, performance, and structure while keeping tests green.
- **Engineering Benefits**:
  - Enforces modular, loosely coupled architecture (untestable monolithic code is impossible to write in TDD).
  - Guarantees high test coverage from day one.
  - Prevents regression bugs and provides developers with the confidence to refactor systems safely.
