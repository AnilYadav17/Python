# 18. Databases with Python: Complete Reference

---

## 1. The Python Database API Specification (PEP 249 / DB-API 2.0)

### What it is
- PEP 249 defines a standard interface specification that all relational database drivers in Python must adhere to:
  - **Connection Objects**: Manage database sessions, transactions, and commits/rollbacks (`conn.commit()`, `conn.rollback()`, `conn.close()`).
  - **Cursor Objects**: Manage query execution context and result iteration (`cursor.execute()`, `cursor.executemany()`, `cursor.fetchone()`, `cursor.fetchall()`).
  - Standard exception hierarchy (`DatabaseError`, `OperationalError`, `IntegrityError`, `DataError`).

### Why it matters
- Portability: Code written using standard DB-API patterns for SQLite can easily be adapted for PostgreSQL (`psycopg`), MySQL (`mysql-connector`), or Oracle with minimal driver changes.

### How it works (internals, if relevant)
- `cursor.execute(sql, params)` prepares the query statement and binds parameters at the driver level before transmission to the database engine.
- Results are retrieved in chunks or streamed from the server buffer:
  - `fetchone()`: Returns next row as a tuple (or `None`).
  - `fetchmany(size)`: Returns list of up to `size` rows.
  - `fetchall()`: Retrieves all remaining rows into memory at once.

### Common mistakes / gotchas
- Using `fetchall()` on tables with millions of rows: loads all rows into Python memory at once, triggering a `MemoryError`. Stream using `fetchone()` or iterate over the cursor directly (`for row in cursor:`).
- Forgetting to close cursors or connections, leaking database server connection pool slots.

### Connects to
- Embedded Databases with `sqlite3` (subtopic 2 below).

---

## 2. Embedded Databases with `sqlite3`

### What it is
- A complete, self-contained, serverless zero-configuration SQL database engine included in Python's standard library.
- Connection:
  - Disk-based: `conn = sqlite3.connect("database.db")`
  - In-memory: `conn = sqlite3.connect(":memory:")` (lives purely in RAM; destroyed on close).
- **Row Factory**: By default, SQLite returns rows as plain tuples. Setting `conn.row_factory = sqlite3.Row` allows accessing columns by name like a dictionary (`row["username"]`).

### Why it matters
- Requires zero external database server setup or docker containers.
- Perfect for local development, desktop applications, embedded systems, caching, and automated integration tests.

### How it works (internals, if relevant)
- SQLite stores an entire relational database in a single cross-platform disk file.
- Reads are concurrent (multiple processes can read simultaneously); writes lock the database file using OS file locks.

### Common mistakes / gotchas
- Concurrent write locking: Multiple processes trying to write to SQLite simultaneously will encounter `sqlite3.OperationalError: database is locked`. For high-concurrency writes, use client-server databases (PostgreSQL/MySQL).
- Forgetting that SQLite types are dynamic (type affinity): SQLite will allow inserting a string into an `INTEGER` column unless strict mode is enabled.

### Connects to
- SQL Injection Prevention (subtopic 3 below).

---

## 3. SQL Injection Prevention & Parameterized Queries

### What it is
- **SQL Injection (SQLi)**: A critical security vulnerability where untrusted user input is directly concatenated or formatted into a SQL query string, allowing attackers to manipulate query structure, bypass authentication, steal data, or drop tables.
- **Vulnerable Antipattern**:
  ```python
  # CATASTROPHIC SECURITY BUG:
  cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")
  ```
  If `user_input` is `' OR '1'='1`, the query returns all users!
- **Parameterized Query (The Solution)**:
  ```python
  # SECURE:
  cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
  ```

### Why it matters
- SQL Injection remains one of the OWASP Top 10 most destructive vulnerabilities in web applications.
- Parameterized queries are mandatory for all production code without exception.

### How it works (internals, if relevant)
- Parameterized queries send the SQL statement template to the database engine first to be parsed and compiled into an execution plan.
- Parameter values are sent separately across the wire and treated strictly as literal data, never as executable SQL tokens.
- Parameter placeholder styles across drivers:
  - `qmark` (`?`): Used by `sqlite3`.
  - `format` / `pyformat` (`%s`): Used by MySQL and PostgreSQL.
  - `named` (`:name`): Used by SQLAlchemy and SQLite.

### Common mistakes / gotchas
- Using string formatting inside parameterized queries: `cursor.execute("SELECT * FROM %s WHERE id = ?" % table_name, (1,))`. Table names and column names **cannot** be parameterized by DB-API! Only values can be parameterized.
- Passing parameters as a single item without a tuple: `cursor.execute("SELECT * FROM users WHERE id = ?", (42,))` requires a trailing comma for single-element tuples!

### Connects to
- Transaction Management & ACID (subtopic 4 below).

---

## 4. Transaction Management & ACID Guarantees

### What it is
- A **transaction** is a sequence of one or more database operations executed as a single logical unit of work adhering to **ACID** properties:
  - **A — Atomicity**: "All or nothing." If any statement fails, the entire transaction is rolled back.
  - **C — Consistency**: Data must transition from one valid state to another, preserving all constraints and foreign keys.
  - **I — Isolation**: Concurrent transactions execute without interfering with one another.
  - **D — Durability**: Once committed, changes survive system crashes or power failures.

### Why it matters
- Essential for financial transfers, e-commerce order checkouts, inventory reservation, and multi-table mutations.

### How it works (internals, if relevant)
- In Python DB-API, transactions are started implicitly on the first DML statement (`INSERT`, `UPDATE`, `DELETE`).
- Changes remain uncommitted in a temporary transaction log (WAL / journal).
- Executing `conn.commit()` flushes changes to durable disk storage.
- Executing `conn.rollback()` discards all pending uncommitted operations.
- Python `sqlite3.Connection` can be used as a context manager:
  ```python
  with conn: # Automatically commits on clean exit, rolls back on exception!
      cursor.execute(...)
  ```

### Common mistakes / gotchas
- Forgetting to call `conn.commit()`: Python terminates and the database rolls back all uncommitted changes, resulting in silent data loss!
- Catching exceptions inside a transaction block without calling `conn.rollback()`, leaving the connection in an uncommitted, dirty state.

### Connects to
- Relational Database Connectors & Connection Pooling (subtopic 5 below).

---

## 5. Relational Database Connectors & Connection Pooling

### What it is
- Connecting Python to production enterprise database servers:
  - **PostgreSQL**: `psycopg2` (standard C-extension), `psycopg` (modern Psycopg 3 with native async support), `asyncpg` (ultra-fast pure async driver).
  - **MySQL**: `mysql-connector-python`, `PyMySQL`.
- **Connection Pooling**: Maintaining a cache of pre-opened, persistent database connections that are borrowed by request threads and returned when done.

### Why it matters
- Establishing a new TCP handshake, TLS negotiation, and database authentication on every HTTP request takes 50–100ms and rapidly exhausts database connection limits (`max_connections = 100`).
- Connection pools reduce connection acquisition latency to sub-millisecond speeds.

### How it works (internals, if relevant)
- A thread-safe pool queue manages $N$ active connection objects.
- A worker calls `pool.getconn()`, runs queries, and calls `pool.putconn(conn)` in a `finally` block to return the connection.

### Common mistakes / gotchas
- Forgetting to return a connection to the pool, causing "Connection Pool Exhaustion" where all incoming web requests hang permanently waiting for an available connection.
- Sharing a single raw connection object across multiple concurrent threads simultaneously without synchronization (DB-API connections are not thread-safe).

### Connects to
- Object-Relational Mapping (ORM) & SQLAlchemy (subtopic 6 below).

---

## 6. Object-Relational Mapping (ORM) & SQLAlchemy

### What it is
- **ORM (Object-Relational Mapping)**: An architectural layer that maps database tables to Python classes, table rows to Python objects, and SQL queries to Python method calls.
- **SQLAlchemy**: The industry-standard Python SQL toolkit and ORM:
  - **Core Layer**: SQL Expression Language, Schema definitions, Connection engine.
  - **ORM Layer**: Declarative models (`DeclarativeBase`), Unit of Work pattern (`Session`), Relationships (`relationship`, foreign keys).

### Why it matters
- Write database code in clean, idiomatic Python without writing raw SQL strings.
- Database Agnostic: The same models and queries run on SQLite, PostgreSQL, MySQL, and Oracle without changing query syntax.
- Protects automatically against SQL injection by parameterizing all queries behind the scenes.

### How it works (internals, if relevant)
- **Declarative Base**: Subclassing `DeclarativeBase` maps class attributes (`mapped_column`) to database schema column descriptors.
- **Session (Unit of Work)**: Tracks changes made to mapped objects in memory (`session.add(user)`, `user.email = "new@email.com"`). Calling `session.commit()` computes the minimal SQL diff (`UPDATE`, `INSERT`) and executes it inside a single transaction.

### Common mistakes / gotchas
- **The N+1 Query Problem**: Iterating through a list of 100 users and accessing `user.orders` without eager loading triggers 1 initial query + 100 separate queries to fetch orders! Fix: Use joined loading (`select(User).options(joinedload(User.orders))`).
- Using an ORM for everything: Complex multi-table reporting queries or bulk data ingestion ($> 100,000$ rows) run significantly faster using raw SQL or SQLAlchemy Core rather than heavyweight ORM object instantiation.

### Connects to
- Intro to Flask (Topic 20) for Flask-SQLAlchemy integration.
