# Project 07: Tested CLI Application (`syspulse`)

A modular, production-ready Command-Line Interface demonstrating Dependency Inversion and automated mock testing.

---

## Architecture
- **Dependency Injection**: The core CLI runner receives a `MetricsCollector` protocol rather than calling hardware APIs directly.
- **Strict Exit Codes**:
  - `0`: All systems OK
  - `1`: Warning threshold exceeded (e.g. RAM > 75%)
  - `2`: Critical threshold exceeded (e.g. RAM > 90% or Disk > 90%)
- **Machine & Human Interfaces**: Supports human-readable terminal output and `--json` format.

---

## Testing
Run unit tests:
```bash
python -m unittest test_cli.py
```
