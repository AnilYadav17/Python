# Project 03: Safe File Organizer

A production-grade Python tool to organize cluttered folders by file category with zero risk of data loss.

---

## Key Features
- **Modern `pathlib`**: Safe path resolution and atomic file renames.
- **`--dry-run` Safety**: Preview file operations before executing any changes.
- **Non-Destructive Collision Resolution**: If a file already exists in the target category folder, automatically appends `_1`, `_2`, etc. Never overwrites existing files.
- **Audit Trail**: Saves `organize_audit.json` with timestamps, original paths, file sizes, and destinations.

---

## Usage

### 1. Preview changes (Dry Run)
```bash
python organizer.py /path/to/downloads --dry-run
```

### 2. Execute organization
```bash
python organizer.py /path/to/downloads
```

---

## Testing
Run the test suite:
```bash
python -m unittest test_organizer.py
```
