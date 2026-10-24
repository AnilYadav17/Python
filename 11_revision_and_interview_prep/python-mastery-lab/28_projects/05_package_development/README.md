# Project 05: Reusable Python Package (`pypulse`)

A production-ready, zero-dependency Python package following modern packaging specifications (PEP 517, PEP 518, PEP 621) with strict static typing and explicit `__all__` API boundaries.

---

## Architecture
```
05_package_development/
├── pyproject.toml        # Modern standard build metadata
├── README.md             # Package documentation
├── src/
│   └── pypulse/
│       ├── __init__.py   # Clean public exports (__all__)
│       ├── validators.py # Email, URL, slug validation
│       └── transformers.py # Case conversion, slugify, truncate
└── tests/
    └── test_pypulse.py   # 100% test coverage
```

---

## Installation & Testing
Run tests:
```bash
python -m unittest tests/test_pypulse.py
```
