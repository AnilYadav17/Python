# 06. File Handling — Interview & Viva Questions

---

### Q1: Why is specifying `encoding="utf-8"` critical when opening text files in Python?
**Model Answer:**
- If `encoding` is omitted, Python defaults to the platform-dependent locale encoding returned by `locale.getpreferredencoding()`.
- On Linux and macOS, this is almost always UTF-8, but on Windows, it frequently defaults to legacy single-byte encodings like CP1252 or Windows-1252.
- A script tested on Linux that processes multi-byte Unicode characters (such as emojis, accented letters, or Asian scripts) will crash on Windows with `UnicodeDecodeError` or silently corrupt data. Specifying `encoding="utf-8"` guarantees identical, cross-platform behavior.

---

### Q2: What is the difference between `open(..., 'w+')` and `open(..., 'r+')`?
**Model Answer:**
- Both modes allow reading and writing.
- **`'w+'` (Write & Read)**: **Immediately truncates** the existing file to 0 bytes upon opening! If the file contains existing data, it is destroyed instantly. If the file does not exist, it is created.
- **`'r+'` (Read & Write)**: Opens the existing file **without truncating it**. The file pointer begins at index 0, allowing you to read existing contents and overwrite specific portions in-place using `seek()`. The file must already exist, or a `FileNotFoundError` is raised.

---

### Q3: Why is `newline=""` mandatory when using Python's `csv` module for file writing?
**Model Answer:**
- By default in text mode, Python's Universal Newline mechanism translates line endings (`\n` into the OS standard, such as `\r\n` on Windows).
- However, the `csv` module already includes its own internal newline terminator (RFC 4180 dictates `\r\n`).
- If `newline=""` is not specified, Python applies a second layer of translation on Windows, transforming `\r\n` into `\r\r\n`, which causes every row written to the CSV file to be separated by an unwanted blank empty row. Setting `newline=""` disables Python's outer newline translation.

---

### Q4: How does iterating over a file (`for line in f:`) differ from `f.readlines()` in memory efficiency?
**Model Answer:**
- `f.readlines()` reads the **entire file** into memory at once and constructs a Python list containing every individual line as a separate string object. For large files (e.g. 5 GB), this causes massive memory spikes and risks crashing with a `MemoryError`.
- `for line in f:` uses Python's internal buffered generator/iterator protocol. It reads chunks into a small fixed-size buffer (typically 8 KB) and yields one line at a time on demand. Its memory consumption is constant ($O(1)$ auxiliary memory), regardless of whether the file is 10 KB or 100 GB.

---

### Q5: Why is `pathlib.Path` favored over the legacy `os.path` module in modern Python?
**Model Answer:**
- `os.path` operates purely on raw string manipulations, requiring nested function calls like `os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))`.
- `pathlib.Path` provides a unified, object-oriented API that encapsulates paths into first-class objects.
- Advantages:
  - Intuitive `/` slash operator for joining paths: `Path(__file__).parent.parent / "data"`.
  - Rich properties (`.name`, `.stem`, `.suffix`, `.parent`).
  - Built-in I/O methods (`.read_text()`, `.write_bytes()`, `.mkdir(parents=True)`).
  - Cross-platform portability: automatically instantiates `PosixPath` or `WindowsPath` based on host OS.

---

### Q6: How do you serialize non-standard Python objects (like `datetime.datetime` or custom classes) to JSON?
**Model Answer:**
- Standard JSON only supports primitives (`str`, `int`, `float`, `bool`, `None`, `list`, `dict`).
- Attempting to serialize `datetime` raises `TypeError: Object of type datetime is not JSON serializable`.
- Two idiomatic solutions:
  1. **Supply a `default` function**: Pass a converter callable to `json.dumps(obj, default=serializer)`, which handles unrecognized types (e.g. `if isinstance(o, datetime): return o.isoformat()`).
  2. **Subclass `json.JSONEncoder`**: Override `default(self, o)` to provide custom transformation rules, and pass it via `cls=CustomEncoder`.

---

### Q7: What is an "atomic file write", and why is it important in production systems?
**Model Answer:**
- An atomic file write guarantees that a file is either completely updated with new data or left completely untouched; it is never left in a partially written or corrupted state if the power fails, the process crashes, or the disk fills up mid-write.
- **Pattern**:
  1. Write the new content to a temporary file located in the same filesystem directory.
  2. Flush and close the temporary file.
  3. Use `os.replace(temp_file, target_file)` to swap the temporary file into place.
- On POSIX systems and modern Windows, renaming an existing file within the same filesystem is an atomic OS operation, ensuring concurrent readers never see incomplete half-written data.
