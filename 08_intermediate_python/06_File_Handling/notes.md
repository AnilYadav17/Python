# 06. File Handling: Complete Reference

---

## 1. File Modes and Open Semantics

### What it is
- The built-in `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None)` function returns a file stream object.
- **File Modes**:
  - `'r'`: Read-only (file must exist; default).
  - `'w'`: Write-only (truncates/overwrites file if it exists, creates if absent).
  - `'a'`: Append-only (writes to end of file, creates if absent).
  - `'x'`: Exclusive creation (fails with `FileExistsError` if file exists).
  - `'b'`: Binary mode (operates on raw `bytes` without character decoding).
  - `'t'`: Text mode (default; decodes `bytes` to `str` using specified encoding).
  - `'+'`: Read and write update mode (`'r+'`, `'w+'`, `'a+'`).

### Why it matters
- Selecting the correct mode prevents accidental data loss (e.g. `'w'` instantly wipes out existing file contents upon open).
- Specifying `encoding="utf-8"` is critical for cross-platform portability between Linux (default UTF-8) and Windows (often default cp1252), preventing encoding errors.

### How it works (internals, if relevant)
- Python delegates to the OS `open()` system call, which returns an integer file descriptor (`fd`).
- In text mode, Python wraps the OS stream with `io.TextIOWrapper`, which performs character encoding/decoding and newline translation (`\r\n` <-> `\n`).
- In binary mode, Python returns a buffered raw binary stream (`io.BufferedReader` or `io.BufferedWriter`).

### Common mistakes / gotchas
- Omitting `encoding="utf-8"`: on Windows, Python defaults to the local ANSI code page (e.g. `cp1252`), which crashes with `UnicodeDecodeError` when encountering emojis or non-ASCII characters.
- Using `'w+'` expecting to read an existing file: `'w+'` truncates the file to 0 bytes immediately upon opening! Use `'r+'` instead.

### Connects to
- Stream Operations (subtopic 2 below) and Context Managers (Topic 10).

---

## 2. Stream Operations: Reading, Writing, and Pointer Navigation

### What it is
- **Reading**:
  - `f.read(size=-1)`: Reads entire file (or up to `size` characters/bytes).
  - `f.readline(size=-1)`: Reads a single line including the trailing `\n`.
  - `f.readlines()`: Reads all lines into a list of strings.
  - Iterating over file object: `for line in f:` streams line by line with memory efficiency.
- **Writing**:
  - `f.write(string)`: Writes string to stream, returning number of characters written.
  - `f.writelines(iterable)`: Writes sequence of strings (does NOT automatically append newlines).
- **Pointer Navigation**:
  - `f.tell()`: Returns current stream position in bytes.
  - `f.seek(offset, whence=0)`: Moves stream position. `whence`: 0 (start), 1 (current), 2 (end). In text mode, only `seek(0)` or seeking to a value returned by `tell()` is guaranteed.

### Why it matters
- Reading a multi-gigabyte file with `f.read()` loads the entire file into RAM, crashing the process with `MemoryError`. Iterating `for line in f:` uses an internal buffer to stream line-by-line with $O(1)$ memory.

### How it works (internals, if relevant)
- File streams are buffered in user-space memory (typically 8 KB).
- Calling `f.write()` does not immediately hit the physical disk; it appends to the internal buffer.
- Data is flushed to disk when the buffer fills, when `f.flush()` is called, or when the file is closed.
- Calling `os.fsync(f.fileno())` forces the OS to physically write cached disk buffers to non-volatile storage.

### Common mistakes / gotchas
- Expecting `f.writelines(["a", "b"])` to insert newline characters between items; it writes `"ab"` concatenated together.
- Forgetting that after reading a file, the pointer is at the end (`EOF`). Subsequent `f.read()` calls return `""` unless reset via `f.seek(0)`.

### Connects to
- Large File Streaming (subtopic 7 below).

---

## 3. The `with` Statement & Context Management

### What it is
- The idiomatic Python construct for opening files:
  ```python
  with open("data.txt", "r", encoding="utf-8") as f:
      content = f.read()
  ```
- Ensures the file descriptor is cleanly closed as soon as the block terminates.

### Why it matters
- Guarantees resource cleanup even if exceptions occur inside the block.
- Prevents file descriptor leaks. Operating systems enforce strict limits on open file descriptors per process (`ulimit -n`, typically 1024); leaking descriptors causes `OSError: [Errno 24] Too many open files`.

### How it works (internals, if relevant)
- The file object returned by `open()` implements the context manager protocol:
  - `__enter__()`: returns the file stream object itself.
  - `__exit__(exc_type, exc_val, exc_tb)`: calls `f.close()`, which flushes unwritten buffers and releases the OS file descriptor.
- Works identically to a `try-finally` block under the hood.

### Common mistakes / gotchas
- Accessing the file stream outside the `with` block: `f.read()` raises `ValueError: I/O operation on closed file`.
- Nesting multiple unnecessary `with` blocks; Python supports opening multiple files in a single line: `with open("in.txt") as src, open("out.txt", "w") as dst: ...`.

### Connects to
- Context Managers Deep Dive (Topic 10).

---

## 4. Structured Data: CSV Files

### What it is
- Working with Comma-Separated Values using the standard library `csv` module:
  - `csv.reader(file, delimiter=',')`: Reads rows as lists of strings.
  - `csv.writer(file, delimiter=',')`: Writes rows from iterables.
  - `csv.DictReader(file)`: Reads rows as dictionaries mapping header column names to values.
  - `csv.DictWriter(file, fieldnames=[...])`: Writes dictionaries based on specified field names.

### Why it matters
- The most prevalent tabular exchange format across data science, databases, and enterprise exports.
- Correctly handles quotes, commas inside text fields, escaped characters, and multi-line values that naive string `.split(",")` fails on.

### How it works (internals, if relevant)
- Implements dialect configurations (`csv.excel`, `csv.unix_dialect`) managing quoting rules (`csv.QUOTE_MINIMAL`, `csv.QUOTE_ALL`, `csv.QUOTE_NONNUMERIC`).
- **Critical Requirement**: When opening files for `csv.reader` or `csv.writer`, you **must specify `newline=""`**.
- Without `newline=""`, Python's universal newline translation and the CSV module's internal newline handling conflict, causing blank lines on Windows (`\r\r\n`).

### Common mistakes / gotchas
- Parsing CSV lines manually with `line.split(",")`, which breaks on fields containing commas within quotes (e.g. `"San Francisco, CA"`).
- Omitting `newline=""` in `open()` when writing CSVs.
- Forgetting to call `writer.writeheader()` when using `csv.DictWriter`.

### Connects to
- Databases with Python (Topic 18) for data ingestion.

---

## 5. Structured Data: JSON Files

### What it is
- Working with JavaScript Object Notation (JSON) using the built-in `json` module:
  - **String Serialization**: `json.dumps(obj, indent=2)` (object to string).
  - **String Deserialization**: `json.loads(string)` (string to Python dict/list).
  - **File Serialization**: `json.dump(obj, file_stream, indent=2)`.
  - **File Deserialization**: `json.load(file_stream)`.

### Why it matters
- The universal standard for REST APIs, microservice payloads, configuration files, and document databases.
- Maps natively to Python primitives: JSON Object -> `dict`, JSON Array -> `list`, JSON String -> `str`, Number -> `int`/`float`, Boolean -> `bool`, Null -> `None`.

### How it works (internals, if relevant)
- Implemented in optimized C (`_json`).
- Serializing non-standard types: Types like `datetime.datetime`, `Decimal`, `UUID`, or custom class instances raise `TypeError: Object of type ... is not JSON serializable`.
- Solution: Provide a custom encoder subclassing `json.JSONEncoder` or supply the `default=callable` argument to `json.dump(s)`.

### Common mistakes / gotchas
- Confusing `load`/`dump` (file stream operations) with `loads`/`dumps` (in-memory string operations; the 's' stands for string).
- Single vs Double Quotes: JSON standard mandates double quotes `"` for strings and keys; single quotes `'` in raw strings raise `json.decoder.JSONDecodeError`.
- Serializing tuples: JSON does not have tuples; Python tuples are serialized as JSON arrays, so `loads()` returns them as `list`.

### Connects to
- Intro to Flask (Topic 20) for `jsonify()` and API requests.

---

## 6. Modern Filesystem Paths: `os.path` vs `pathlib.Path`

### What it is
- **`os.path`**: Legacy module providing procedural path manipulation operating on raw strings (`os.path.join`, `os.path.exists`, `os.path.abspath`).
- **`pathlib.Path`** (PEP 428, Python 3.4+): Modern, object-oriented filesystem abstraction:
  - Slash operator for joining paths: `p = Path.cwd() / "data" / "users.json"`.
  - Properties: `p.name` (filename), `p.stem` (filename without extension), `p.suffix` (extension), `p.parent`.
  - Methods: `p.exists()`, `p.is_file()`, `p.is_dir()`, `p.mkdir(parents=True, exist_ok=True)`, `p.read_text(encoding="utf-8")`, `p.write_text(data)`, `p.glob("*.csv")`, `p.rglob("*.py")`.

### Why it matters
- `pathlib` eliminates OS path separator differences (`/` on Linux/macOS vs `\` on Windows).
- Provides expressive, readable code without requiring repetitive `os.path.join()` nesting.

### How it works (internals, if relevant)
- Returns `PosixPath` or `WindowsPath` instances based on host operating system.
- Implements `os.PathLike`, meaning modern `pathlib.Path` objects can be passed directly to built-in functions like `open(path)`.

### Common mistakes / gotchas
- Hardcoding slash characters in string paths (`"dir/subdir/file.txt"` or `"dir\\subdir\\file.txt"`), which causes cross-platform portability bugs. Use `Path("dir") / "subdir" / "file.txt"`.
- Calling `path.mkdir()` without `parents=True, exist_ok=True`, raising `FileNotFoundError` if parent directories are missing, or `FileExistsError` if directory already exists.

### Connects to
- Real-world file pipelines (subtopic 7 below) and Testing (Topic 12).

---

## 7. Large File Processing & Streaming

### What it is
- Techniques for handling large files (gigabytes to terabytes) without exhausting available system RAM:
  - Line streaming: `for line in f:`
  - Chunked binary reading: `iter(functools.partial(f.read, chunk_size), b"")`
  - Generator pipelines for transformation

### Why it matters
- Prevents `MemoryError` and OS Out-Of-Memory (OOM) killer terminations in production data pipelines.
- Keeps memory usage strictly bounded ($O(1)$) regardless of total file size.

### How it works (internals, if relevant)
- When iterating over a file stream in Python, CPython uses an internal read-ahead buffer (default 8 KB) to minimize system call overhead while yielding lines on-demand.
- Chunked reading reads exactly $K$ bytes per iteration directly into a reused buffer.

### Common mistakes / gotchas
- Using `f.readlines()` on large files, which reads every single line into a massive list in RAM all at once.
- Storing intermediate processed results in a growing in-memory list instead of writing directly to an output stream.

### Connects to
- Iterators & Generators (Topic 11) for building streaming pipelines.
