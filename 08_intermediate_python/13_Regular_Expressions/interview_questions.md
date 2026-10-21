# 13. Regular Expressions — Interview & Viva Questions

---

### Q1: What is the fundamental difference between `re.match()`, `re.search()`, and `re.fullmatch()`?
**Model Answer:**
- **`re.match(pattern, string)`**: Restricts matching exclusively to the **beginning (index 0)** of the string. If the pattern occurs anywhere else other than the very start, it returns `None`.
- **`re.search(pattern, string)`**: Scans through the entire string from left to right, returning a `Match` object for the **first location** where the pattern matches anywhere.
- **`re.fullmatch(pattern, string)`**: Requires the **entire string** to match the pattern from start to finish (`^pattern$`). It returns `None` if any leading or trailing characters remain unmatched. It is the preferred method for strict input validation (emails, usernames).

---

### Q2: Why is raw string notation (`r"..."`) always recommended for regex patterns in Python?
**Model Answer:**
- Python string literals use the backslash `\` as an escape character for escape sequences like `\n` (newline), `\t` (tab), or `\b` (ASCII backspace).
- Regular expressions also use the backslash `\` extensively for metacharacters (e.g. `\b` for word boundary, `\d` for digit).
- Without the raw string prefix `r`, Python's lexical analyzer evaluates `"\b"` as ASCII backspace (`0x08`) before passing the string to the `re` engine, causing the word boundary check to fail.
- Raw strings (`r"\b"`) suppress Python's internal escape processing, passing literal backslashes directly to the regex compiler.

---

### Q3: What is the difference between a greedy and a lazy (non-greedy) quantifier?
**Model Answer:**
- **Greedy Quantifiers (`*`, `+`, `{m,n}`)**: Match as **many characters as possible** while still allowing the rest of the pattern to match. For example, matching `<b>.*</b>` on `<b>A</b> and <b>B</b>` greedily matches the entire line from the first `<b>` to the final `</b>`.
- **Lazy Quantifiers (`*?`, `+?`, `{m,n}?`)**: Match as **few characters as possible**, stopping at the earliest possible point where the following token matches. Matching `<b>.*?</b>` on the same text produces two distinct matches: `<b>A</b>` and `<b>B</b>`.

---

### Q4: What is "Catastrophic Backtracking" (ReDoS), and how can it be prevented?
**Model Answer:**
- Catastrophic Backtracking occurs in NFA regex engines when a pattern contains **nested, overlapping, or ambiguous quantifiers** (e.g. `(a+)+$`).
- When matching against a non-matching input ending in a different character (e.g. `"aaaaaa...!"`), the engine attempts every possible permutation of dividing characters between the inner and outer quantifiers.
- The number of backtracking combinations grows exponentially ($O(2^n)$), freezing the CPU for minutes or days and causing a Denial of Service (ReDoS).
- **Prevention**: Avoid nesting quantifiers on overlapping sets; make character classes mutually exclusive; use atomic groups or possessive quantifiers (or validate with linear string operations).

---

### Q5: What are named capturing groups (`(?P<name>...)`), and what advantages do they provide?
**Model Answer:**
- Named capturing groups assign symbolic identifiers to captured substrings instead of relying on positional indices: `r"(?P<year>\d{4})-(?P<month>\d{2})"`.
- **Advantages**:
  1. Self-documenting: Makes complex regex patterns easily readable and maintainable.
  2. Eliminates index drift: Adding or reordering groups in the pattern does not break code relying on numerical indices like `match.group(1)`.
  3. Direct dictionary export: Calling `match.groupdict()` returns a dictionary mapping group names to their matched substrings, ideal for JSON serialization and data ingestion.

---

### Q6: How do Positive and Negative Lookaround assertions work?
**Model Answer:**
- Lookaround assertions are **zero-width assertions**: they check for the presence or absence of patterns without consuming characters or including them in the matched substring.
- **Positive Lookahead `(?=...)`**: Asserts that the subpattern immediately follows the current position.
- **Negative Lookahead `(?!...)`**: Asserts that the subpattern does NOT follow the current position.
- **Positive Lookbehind `(?<=...)`**: Asserts that the subpattern immediately precedes the current position (must be fixed width in Python `re`).
- **Negative Lookbehind `(?<!...)`**: Asserts that the subpattern does NOT precede the current position.
- Common use case: extracting amounts preceded by a symbol without capturing the symbol: `(?<=\$)\d+`.

---

### Q7: Why does `re.split()` behave differently when using capturing groups `()` vs non-capturing groups `(?:...)`?
**Model Answer:**
- When `re.split(pattern, string)` splits on a pattern that contains standard **capturing groups `()`**, Python includes the matched delimiter substrings in the returned result list.
- When the pattern uses **non-capturing groups `(?:...)`**, Python splits on the pattern and discards the delimiters, returning only the tokens.
- Example:
  - `re.split(r"([,;])", "a,b;c")` yields `['a', ',', 'b', ';', 'c']`.
  - `re.split(r"(?:[,;])", "a,b;c")` yields `['a', 'b', 'c']`.
