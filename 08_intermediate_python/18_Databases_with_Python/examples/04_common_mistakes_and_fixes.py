"""
04_common_mistakes_and_fixes.py
Demonstrates common database programming mistakes:
1. Forgetting to commit (silent data loss)
2. Parameterizing non-value identifiers (table names)
"""

import sqlite3

def mistake_1_forgotten_commit():
    print("--- 1. Forgotten commit() Trap ---")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE audit (msg TEXT);")

    # Insert without calling conn.commit()
    cursor.execute("INSERT INTO audit VALUES ('Action 1');")
    # If connection closes without commit, the transaction is rolled back!
    # Fix: Always call conn.commit() or use 'with conn:' context manager
    conn.commit()
    print("Fix: Always use 'with conn:' or call 'conn.commit()'.")
    conn.close()


def mistake_2_parameterizing_table_names():
    print("\n--- 2. Parameterizing Table Names Pitfall ---")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INT);")

    # MISTAKE: Table names and column names CANNOT be parameterized using '?'
    # cursor.execute("SELECT * FROM ?;", ("users",)) -> sqlite3.OperationalError: near "?": syntax error

    # FIX: Whitelist valid table names before formatting into query
    VALID_TABLES = {"users", "orders", "inventory"}
    table_requested = "users"

    if table_requested in VALID_TABLES:
        query = f"SELECT * FROM {table_requested};"
        cursor.execute(query)
        print(f"Fixed: Whitelisted table '{table_requested}' queried safely.")
    conn.close()


def main():
    mistake_1_forgotten_commit()
    mistake_2_parameterizing_table_names()

if __name__ == "__main__":
    main()
