# 13. Regular Expressions: Complete Reference

---

## 1. The Regex Engine & `re.compile()`

### What it is
- Regular expressions (regex) define search patterns for matching, extracting, and manipulating string data.
- Python provides the built-in `re` module implemented via an optimized C-level backtracking engine (Nondeterministic Finite Automaton / NFA).
- `re.compile(pattern, flags=0)`: Pre-compiles a regex string into a reusable `Pattern` object (`re.Pattern`).

### Why it matters
- Pre-compiling regex patterns that are evaluated inside tight loops or high-throughput request handlers eliminates repeated pattern parsing and bytecode compilation overhead.
- Flags: `re.IGNORECASE` (`re.I`), `re.MULTILINE` (`re.M`), `re.DOTALL` (`re.S`, makes `.` match newline `\n`), `re.VERBOSE` (`re.X`, allows comments and whitespace in complex regex patterns).

### How it works (internals, if relevant)
- The module-level functions (`re.search(pat, s)`) maintain an internal LRU cache (typically 512 compiled patterns).
- Explicitly calling `pat = re.compile(...)` guarantees deterministic reuse without cache eviction risks and makes intentions clear.

### Common mistakes / gotchas
- Forgetting to use Python **raw string notation (`r"..."`)**: without `r`, backslashes are interpreted as Python escape characters (e.g. `"\b"` becomes ASCII backspace 0x08 instead of regex word boundary `\b`). Always write `r"\bword\b"`.

### Connects to
- Core Regex Functions (subtopic 2 below).

---

## 2. Core Regex Functions: `match` vs `search` vs `fullmatch` vs `findall` vs `finditer`

### What it is
- Core matching functions:
  - **`re.match(pattern, string)`**: Matches pattern **only at the beginning** of the string. Returns `Match` object or `None`.
  - **`re.search(pattern, string)`**: Scans through the entire string to find the **first location** where the pattern matches.
  - **`re.fullmatch(pattern, string)`**: Matches if and only if the **entire string** matches the pattern from start to finish.
  - **`re.findall(pattern, string)`**: Returns all non-overlapping matches as a list of strings (or tuples of groups).
  - **`re.finditer(pattern, string)`**: Returns an iterator yielding `Match` objects for all matches (lazy, memory-efficient).
  - **`re.sub(pattern, repl, string, count=0)`**: Replaces occurrences with replacement string or callable function.
  - **`re.split(pattern, string, maxsplit=0)`**: Splits string by occurrences of the pattern.

### Why it matters
- Using `re.match()` when you intended `re.search()` causes false negatives when the target token appears later in the string.
- Using `re.search()` when validating input (like an email or phone) allows malicious trailing characters unless anchors are used; `re.fullmatch()` guarantees complete input validation.

### How it works (internals, if relevant)
- A `Match` object provides:
  - `.group(0)`: Full matched substring.
  - `.group(1, 2, ...)`: Specific captured groups.
  - `.start()`, `.end()`, `.span()`: Exact character indices in the source string.

### Common mistakes / gotchas
- Calling `.group()` directly on the result of `re.search()` without checking if it returned `None`, raising `AttributeError: 'NoneType' object has no attribute 'group'`.
- Using `re.findall()` on patterns with multiple groups: it returns a list of tuples, not flat strings.

### Connects to
- Metacharacters and Character Classes (subtopic 3 below).

---

## 3. Metacharacters, Anchors, and Character Classes

### What it is
- **Anchors**:
  - `^`: Matches start of string (or start of line in `MULTILINE` mode).
  - `$`: Matches end of string (or end of line in `MULTILINE` mode).
  - `\b`: Word boundary (transition between word char `\w` and non-word char `\W`).
  - `\B`: Non-word boundary.
- **Character Classes**:
  - `.`: Matches any character except newline (matches newline if `re.DOTALL` is set).
  - `\d`: Any Unicode decimal digit (`[0-9]`). `\D`: Any non-digit.
  - `\w`: Any word character (alphanumeric + underscore). `\W`: Any non-word character.
  - `\s`: Any whitespace character (space, tab, newline `\r\n\t\f\v`). `\S`: Non-whitespace.
  - Custom Set `[abc]`: Matches `a`, `b`, or `c`.
  - Range `[a-z0-9]`: Matches lowercase letters and digits.
  - Negation `[^0-9]`: Matches any character *except* digits.

### Why it matters
- Forms the core syntax for targeting precise character subsets and structural text boundaries.

### How it works (internals, if relevant)
- Character classes are converted into bit vectors during regex compilation for $O(1)$ character membership testing.

### Common mistakes / gotchas
- Placing a hyphen `-` inside a custom class in an ambiguous position: `[a-c]` defines a range ($a, b, c$), whereas `[ac-]` or `[-ac]` treats hyphen as a literal character.
- Escaping unnecessary characters inside `[]`: most metacharacters (like `.` or `*`) lose their special meaning inside square brackets and are treated as literals (e.g. `[.]` matches a literal dot).

### Connects to
- Quantifiers (subtopic 4 below).

---

## 4. Quantifiers: Greedy vs Lazy & Catastrophic Backtracking

### What it is
- Quantifiers specify repetition:
  - **Greedy (Default)**: Matches as many characters as possible.
    - `*`: 0 or more.
    - `+`: 1 or more.
    - `?`: 0 or 1.
    - `{m,n}`: Between $m$ and $n$ repetitions.
  - **Lazy / Non-Greedy (`?` suffix)**: Matches as few characters as possible.
    - `*?`, `+?`, `??`, `{m,n}?`.

### Why it matters
- Greedy quantifiers routinely match too much text in structured documents (e.g. matching from the first HTML tag to the last HTML tag across an entire file).
- Poorly constructed nested quantifiers can cause **Catastrophic Backtracking (Regular Expression Denial of Service / ReDoS)**, freezing the CPU for hours or days.

### How it works (internals, if relevant)
- The backtracking engine pushes decision state points onto an internal stack.
- When an attempt fails, it backtracks to the previous decision point and tries the next branch.
- If a pattern contains nested quantifiers like `(a+)+$`, matching against an input of `"aaaa...a!"` causes $O(2^n)$ exponential backtracking attempts, pegging CPU at 100%.

### Common mistakes / gotchas
- Using greedy `.*` when parsing HTML/XML (e.g. `<.*>` matches from the first `<` to the very last `>` on the page). Fix: Use non-greedy `<.*?>` or negated class `<[^>]+>`.
- Writing unbounded nested quantifiers on user-submitted text.

### Connects to
- Groups and Capturing (subtopic 5 below).

---

## 5. Groups and Capturing

### What it is
- Mechanisms to segment matched text into distinct semantic tokens:
  - **Numbered Capturing Groups `(...)`**: Captures matched subpattern accessible via `match.group(1)`, `match.group(2)`.
  - **Named Capturing Groups `(?P<name>...)`**: Captures matched subpattern accessible via `match.group('name')` or as a dictionary via `match.groupdict()`.
  - **Non-Capturing Groups `(?:...)`**: Groups subpatterns for repetition or alternatives without allocating capturing overhead or appearing in `match.groups()`.
  - **Backreferences (`\1`, `(?P=name)`)**: Matches the identical text previously captured by that group earlier in the regex.

### Why it matters
- Named groups make regex patterns self-documenting and directly serializable into dictionaries and data models.
- Non-capturing groups improve performance and keep output groups clean.

### How it works (internals, if relevant)
- Capturing groups record start and end byte offsets in the string during matching.
- Non-capturing groups `(?:...)` only group tokens logically without allocating slot indices in the match result array.

### Common mistakes / gotchas
- Using capturing groups `()` inside `re.split()`: causes the delimiters themselves to be included in the returned list! Use non-capturing `(?:...)` to split cleanly without keeping delimiters.
- Numbered group index drift when refactoring: adding a new group shifts all subsequent group indices (`group(3)` becomes `group(4)`). Use named groups `(?P<name>...)` to eliminate this bug.

### Connects to
- Lookaround Assertions (subtopic 6 below).

---

## 6. Lookaround Assertions

### What it is
- **Zero-width assertions** that match characters without consuming them or including them in the match result:
  - **Positive Lookahead `(?=...)`**: Asserts that what follows immediately matches pattern.
  - **Negative Lookahead `(?!...)`**: Asserts that what follows immediately does NOT match pattern.
  - **Positive Lookbehind `(?<=...)`**: Asserts that what precedes immediately matches pattern.
  - **Negative Lookbehind `(?<!...)`**: Asserts that what precedes immediately does NOT match pattern.

### Why it matters
- Enables complex conditional validation: password policies (requiring at least one digit, one uppercase letter, one special character in any order).
- Extracts values conditioned on prefixes/suffixes without including the prefix/suffix in the match (e.g. extract numeric price from `$150.00`).

### How it works (internals, if relevant)
- The engine checks the condition at the current position. If satisfied, it advances matching *without moving the string pointer*.
- In standard Python `re`, **lookbehind assertions must have a fixed, predetermined width** (e.g. `(?<=https://)` is valid; `(?<=https?://)` raises `re.error: look-behind requires fixed-width pattern`).

### Common mistakes / gotchas
- Attempting variable-length patterns (like `.*` or `+`) inside lookbehinds in standard `re`.

### Connects to
- Real-World Practical Patterns (subtopic 7 below).

---

## 7. Real-World Practical Patterns

### What it is
- Standard production regex applications:
  - **Email Validation**: Comprehensive format checking without fragile oversimplifications.
  - **Log Parsing**: Apache/Nginx combined access log scraping into structured JSON.
  - **Data Masking / Redaction**: Scrubbing Social Security Numbers, Credit Cards, or API keys with `re.sub()`.
  - **URL Parameter Extraction**: Parsing query strings, slugs, and domains.

### Why it matters
- Core tasks across backend engineering, security auditing, data ingestion, and web scraping.

### How it works (internals, if relevant)
- `re.sub(pattern, replacement_callable, text)`: Passing a function as the replacement argument allows dynamic, programmatic replacement logic based on the match object.

### Common mistakes / gotchas
- Using regex to parse full HTML or XML documents: HTML is a context-free grammar that cannot be fully parsed by regular expressions (leads to parsing bugs on nested elements). Use HTML parsers (`BeautifulSoup`, `lxml`) instead.

### Connects to
- Type Hints (Topic 14) and Flask Route Parsing (Topic 20).
