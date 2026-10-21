"""
01_basic_usage.py
Demonstrates core SQLite database operations in Python:
- Connecting to in-memory database
- Schema creation with DDL
- Inserting single and batch records (executemany)
- Accessing columns as dictionaries using sqlite3.Row
"""

import sqlite3

def setup_database():
    # Connect to in-memory database for testing
    conn = sqlite3.connect(":memory:")
    # Enable dict-like column access by name
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    return conn


def populate_and_query(conn):
    cursor = conn.cursor()

    # 1. Insert single record using parameterized query (?)
    cursor.execute(
        "INSERT INTO users (username, email, role) VALUES (?, ?, ?);",
        ("alice", "alice@enterprise.com", "admin")
    )

    # 2. Batch insertion using executemany()
    batch_data = [
        ("bob", "bob@enterprise.com", "developer"),
        ("charlie", "charlie@enterprise.com", "designer"),
        ("diana", "diana@enterprise.com", "manager")
    ]
    cursor.executemany(
        "INSERT INTO users (username, email, role) VALUES (?, ?, ?);",
        batch_data
    )
    conn.commit()

    # 3. Query all users and access via sqlite3.Row
    print("--- Querying Users with sqlite3.Row ---")
    cursor.execute("SELECT id, username, email, role FROM users ORDER BY id ASC;")
    rows = cursor.fetchall()

    for row in rows:
        # Access by column name like a dict or by index like a tuple
        print(f"  [User #{row['id']}] {row['username']:<10} | Email: {row['email']:<24} | Role: {row['role']}")


def main():
    conn = setup_database()
    try:
        populate_and_query(conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
