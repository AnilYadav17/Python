# 12. Testing: Complete Reference

---

## 1. Testing Foundations & Test-Driven Development (TDD)

### What it is
- Software verification practices that ensure code correctness, prevent regressions, and enforce architectural design contracts:
  - **Unit Testing**: Verifies isolated units of code (single functions, methods, classes) in complete isolation from external dependencies.
  - **Integration Testing**: Verifies communication between multiple integrated components (database queries, service interactions, filesystem I/O).
  - **End-to-End (E2E) Testing**: Verifies entire system workflows from user input to final output.
- **TDD (Test-Driven Development)**: Software development workflow following the **Red-Green-Refactor** cycle:
  1. **Red**: Write a failing unit test specifying desired behavior before implementing any code.
  2. **Green**: Write the minimum amount of code necessary to make the test pass.
  3. **Refactor**: Clean up the code, optimize performance, and remove duplication while tests remain green.

### Why it matters
- Prevents silent regressions when modifying legacy code.
- Forces developers to write modular, loosely coupled, and testable interfaces.
- Serves as living, executable documentation of software requirements.

### How it works (internals, if relevant)
- Tests operate by establishing an initial state (Arrange), invoking the target behavior (Act), and verifying the resulting state or return value against expectations (Assert) — the AAA pattern.

### Common mistakes / gotchas
- Writing tests that test implementation details (private methods, variable names) rather than observable behavior and public interfaces.
- Testing multiple unrelated concepts in a single unit test, making it difficult to pinpoint the root cause of failures.

### Connects to
- The `unittest` Framework (subtopic 2 below) and `pytest` (subtopic 3).

---

## 2. The `unittest` Framework

### What it is
- Python's built-in testing framework inspired by Java's JUnit:
  - Inherits from `unittest.TestCase`.
  - Lifecycle hooks: `setUp()`, `tearDown()`, `setUpClass()`, `tearDownClass()`.
  - Assertion methods: `self.assertEqual(a, b)`, `self.assertTrue(x)`, `self.assertFalse(x)`, `self.assertIn(a, b)`, `self.assertAlmostEqual(a, b)`, `self.assertRaises(Exc)`.
  - Execution: `unittest.main()` or `python -m unittest discover`.

### Why it matters
- Included out-of-the-box in the standard library with zero external dependencies.
- Standard framework used in enterprise Python codebases and standard library testing.

### How it works (internals, if relevant)
- Test discovery: Scans for classes subclassing `TestCase` and identifies methods starting with the prefix `test_`.
- Isolation: A brand new `TestCase` instance is instantiated for *every single test method*, ensuring test isolation.
- `setUp()` runs immediately before each test method; `tearDown()` runs immediately after each test method (even if the test failed).

### Common mistakes / gotchas
- Forgetting the `test_` prefix on method names: any method not prefixed with `test_` is silently ignored and never executed by the test runner.
- Putting shared mutable setup in `setUpClass()` without resetting it, causing state contamination across tests.

### Connects to
- The `pytest` Framework (subtopic 3 below).

---

## 3. The `pytest` Framework

### What it is
- The de facto modern standard third-party testing framework in the Python ecosystem:
  - Eliminates class boilerplate: tests are simple functions prefixed with `test_`.
  - Native Python `assert` statement: no need for dozens of `self.assert*` methods.
  - Automatic test discovery: matches files named `test_*.py` or `*_test.py`.
  - Rich ecosystem of plugins (`pytest-cov`, `pytest-asyncio`, `pytest-mock`, `pytest-xdist`).

### Why it matters
- Drastically less boilerplate than `unittest`.
- Advanced **assertion rewriting**: when an assertion fails, `pytest` inspects the AST (Abstract Syntax Tree) to display exact intermediate values of sub-expressions in failure diffs.

### How it works (internals, if relevant)
- Pytest hooks into Python's import system (`sys.meta_path`). When loading test files, it intercepts the bytecode compiler and rewrites standard `assert expr` statements into rich diagnostic introspection routines.
- Supports markers (`@pytest.mark.skip`, `@pytest.mark.xfail`, custom tags) to filter and organize test runs.

### Common mistakes / gotchas
- Overusing class wrappers in `pytest` when simple standalone functions are more idiomatic.
- Naming helper functions with the `test_` prefix, causing pytest to mistakenly execute them as test cases.

### Connects to
- Pytest Fixtures (subtopic 4 below).

---

## 4. Pytest Fixtures & Dependency Injection

### What it is
- A mechanism for setting up and tearing down baseline test environments and dependencies:
  - Decorated with `@pytest.fixture`.
  - Passed directly into test functions as named arguments (Dependency Injection).
  - Teardown logic implemented cleanly using `yield`.
  - Scopes: `function` (default, runs per test), `class`, `module`, `session` (runs once per entire test suite).

### Why it matters
- Replaces rigid `setUp`/`tearDown` inheritance hierarchies with modular, composable fixture components.
- Fixtures can depend on other fixtures, building complex dependency graphs effortlessly.

### How it works (internals, if relevant)
- Pytest analyzes test function parameter names via reflection (`inspect.signature`).
- When a parameter matches a registered fixture name, pytest evaluates the fixture before the test and injects the yielded value.
- When the test completes, execution resumes after `yield` in the fixture to perform cleanup.

### Common mistakes / gotchas
- Using session-scoped fixtures for mutable data, causing cross-test state pollution.
- Forgetting that code after `yield` in a fixture will not run if an unhandled exception occurred *before* the `yield`.

### Connects to
- Parameterized Testing (subtopic 5 below).

---

## 5. Parameterized Testing

### What it is
- Running a single test function against a table of multiple distinct inputs and expected outputs.
- In `pytest`: `@pytest.mark.parametrize("input_val, expected", [(val1, exp1), (val2, exp2), ...])`.
- In `unittest`: `self.subTest()` context manager.

### Why it matters
- Eliminates duplicate copy-pasted test code when validating edge cases, boundary conditions, and invalid inputs.
- Generates a distinct, independent test report for each parameter tuple: if one input fails, remaining inputs continue executing.

### How it works (internals, if relevant)
- Pytest dynamically generates distinct test node IDs for each parameter row at test collection time.

### Common mistakes / gotchas
- Testing multiple test cases inside a standard loop without `subTest` or `parametrize`: if the first iteration fails, the entire test crashes and remaining test cases are never evaluated!

### Connects to
- Mocking Basics (subtopic 6 below).

---

## 6. Mocking Basics with `unittest.mock`

### What it is
- Standard library tools to replace real system components with test doubles:
  - **`Mock`**: Generic callable object that records all calls, arguments, and return values.
  - **`MagicMock`**: Subclass of `Mock` pre-configured with implementations for all Python magic/dunder methods (`__len__`, `__iter__`, `__getitem__`, `__enter__`, `__exit__`).
  - **`@patch` / `patch.object`**: Temporarily swaps an object or attribute during test execution and restores the original upon completion.
  - Assertions: `mock.assert_called()`, `mock.assert_called_once()`, `mock.assert_called_once_with(*args, **kwargs)`.

### Why it matters
- Isolates unit tests from slow, unreliable, or external network/disk resources (payment gateways, third-party APIs, email servers).
- Allows simulating rare edge cases and transient network failures (`side_effect = TimeoutError`).

### How it works (internals, if relevant)
- **The Target Path Rule**: *Patch where an object is LOOKED UP, not where it is defined.*
  If `app.py` has `from services import client`, you must patch `'app.client'`, NOT `'services.client'`.
- `patch()` acts as both a function decorator and a context manager, restoring original references in its `finally` block.

### Common mistakes / gotchas
- Patching the wrong location (patching the module of definition instead of the importing namespace).
- Typos in mock assertions: e.g. writing `mock.assert_called_once_with()` vs accidentally inventing methods like `mock.assert_was_called()` (which does NOT exist and passes silently because `Mock` creates attributes dynamically!). Use `create_autospec=True` to prevent this.
- **Over-mocking**: Mocking so many internal details that the test passes even when the underlying software is completely broken.

### Connects to
- Test Doubles & Best Practices (subtopic 7 below).

---

## 7. Test Doubles & Best Practices

### What it is
- Taxonomy of Test Doubles (Gerard Meszaros):
  - **Dummy**: Passed around but never actually used (e.g. filler parameter).
  - **Stub**: Provides pre-canned answers to calls made during the test.
  - **Spy**: A stub that additionally records information about how it was called.
  - **Mock**: Pre-programmed with expectations of calls it should receive; verifies behavior.
  - **Fake**: Has a working implementation, but takes shortcuts (e.g. in-memory SQLite instead of production PostgreSQL).

### Why it matters
- Choosing the right test double keeps tests fast, reliable, and decoupled from internal refactorings.

### How it works (internals, if relevant)
- Code Coverage (`coverage.py`): Measures the percentage of lines, branches, and statements executed during test runs (`coverage run -m pytest && coverage report`).

### Common mistakes / gotchas
- Aiming for 100% test coverage by writing low-quality, trivial tests that test language built-ins rather than domain invariants.
- Writing brittle tests tightly coupled to internal implementation private methods instead of public contracts.

### Connects to
- Regular Expressions (Topic 13) and Virtual Environments (Topic 15).
