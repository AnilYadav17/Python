# Lesson 23.1: Database Programming — SQLite, DB-API 2.0 & The Repository Pattern

## 1. What Is This in Simple Words?
Applications need persistent, structured memory that survives server restarts:
- **`sqlite3`**: A full, serverless SQL database engine built right into Python's standard library. No server installation or configuration needed!
- **DB-API 2.0 (PEP 249)**: Python's official database standard. Whether you use SQLite, PostgreSQL (`psycopg`), or MySQL (`mysql-connector`), the functions (`connect`, `cursor`, `execute`, `fetchall`) work the exact same way!
- **Repository Pattern**: An enterprise design pattern where all SQL queries live in dedicated repository classes, keeping your core business logic clean, testable, and SQL-free.

---

## 2. Using `sqlite3` the Professional Way

### Safe Transactions with Context Managers:
When used as a context manager (`with conn:`), SQLite automatically calls `commit()` on success, or `rollback()` if an error occurs:

```python
import sqlite3
from dataclasses import dataclass

@dataclass
class User:
    id: int | None
    username: str
    email: str

def init_db(conn: sqlite3.Connection):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL
            );
        """)

# In-memory database for testing:
conn = sqlite3.connect(":memory:")
init_db(conn)
```

---

## 3. Implementing the Repository Pattern

Don't sprinkle `conn.execute(...)` all over your application! Wrap it cleanly:

```python
class UserRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create(self, username: str, email: str) -> User:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO users (username, email) VALUES (?, ?)",
                (username, email)
            )
            return User(id=cursor.lastrowid, username=username, email=email)

    def find_by_username(self, username: str) -> User | None:
        cursor = self.conn.execute(
            "SELECT id, username, email FROM users WHERE username = ?",
            (username,)
        )
        row = cursor.fetchone()
        if row:
            return User(id=row[0], username=row[1], email=row[2])
        return None

# Usage:
repo = UserRepository(conn)
new_user = repo.create("anil", "anil@example.com")
print(f"Created user with ID: {new_user.id}")

found = repo.find_by_username("anil")
print(f"Retrieved: {found.username} -> {found.email}")
```

---

## 4. Mind-Blowing Facts! 💡

> **Fact 1: SQLite Can Handle 100,000 Requests/Sec!**  
> Beginners mistakenly think SQLite is a "toy". In reality, SQLite powers the Airbus A350 flight software, iOS and Android smartphones, Apple Photos, and is the most widely deployed database engine on Earth! When configured with `PRAGMA journal_mode=WAL;` (Write-Ahead Logging), SQLite supports concurrent readers and handles incredible throughput!
>
> **Fact 2: Row Factories!**  
> By default, `sqlite3` returns plain tuples (`(1, 'anil', 'email')`). But if you set:  
> `conn.row_factory = sqlite3.Row`  
> you can access columns by their database column names: `row["username"]` just like a dictionary!

---

## 5. Self-Test
1. **Question**: What happens if an unhandled exception occurs inside a `with conn:` block in `sqlite3`?
   - *Answer*: Python's SQLite context manager automatically rolls back all uncommitted changes, ensuring database consistency (ACID atomicity).
