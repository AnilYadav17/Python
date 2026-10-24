# Project 08: Database Application & Repository Pattern

An enterprise data access layer demonstrating DB-API 2.0 best practices, schema migration tracking, and Unit-of-Work transaction management.

---

## Architectural Highlights
- **Migration Manager**: Automatically versions and executes migrations with a `schema_migrations` audit table.
- **Repository Pattern**: All database interactions are encapsulated behind `ProductRepository`, keeping SQL separate from domain models.
- **SQL Injection Immune**: All SQL parameters use positional placeholders (`?`).
- **Unit of Work**: Provides transaction context managers ensuring multi-step operations roll back completely on failure.

---

## Testing
Run unit tests:
```bash
python -m unittest test_db.py
```
