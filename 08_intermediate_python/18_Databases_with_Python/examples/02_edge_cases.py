"""
02_edge_cases.py
Demonstrates database security and constraint edge cases:
1. SQL Injection vulnerability vs Parameterized Query protection
2. Handling integrity constraint violations (sqlite3.IntegrityError)
"""

import sqlite3

def demonstrate_sql_injection():
    print("--- 1. SQL Injection Vulnerability vs Parameterized Defense ---")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE secrets (id INT, account TEXT, pin TEXT);")
    cursor.execute("INSERT INTO secrets VALUES (1, 'Admin', 'SECRET_9999');")
    cursor.execute("INSERT INTO secrets VALUES (2, 'Guest', '1234');")
    conn.commit()

    # Malicious payload designed to bypass authentication
    malicious_input = "' OR '1'='1"

    # VULNERABLE APPROACH: String formatting
    insecure_query = f"SELECT * FROM secrets WHERE account = '{malicious_input}';"
    cursor.execute(insecure_query)
    leaked_rows = cursor.fetchall()
    print(f"Vulnerable Query Result (LEAKED ALL SECRETS!): {leaked_rows}")

    # SECURE APPROACH: Parameterized query
    secure_query = "SELECT * FROM secrets WHERE account = ?;"
    cursor.execute(secure_query, (malicious_input,))
    safe_rows = cursor.fetchall()
    print(f"Secure Query Result (No match found, attack defeated): {safe_rows}")
    conn.close()


def demonstrate_integrity_error():
    print("\n--- 2. Database Constraint Violations ---")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE products (sku TEXT PRIMARY KEY, price REAL CHECK(price >= 0));")

    cursor.execute("INSERT INTO products VALUES ('SKU-001', 19.99);")
    conn.commit()

    # Case A: Duplicate Primary Key
    try:
        cursor.execute("INSERT INTO products VALUES ('SKU-001', 29.99);")
        conn.commit()
    except sqlite3.IntegrityError as err:
        print(f"Caught expected Unique Constraint Failure: {err}")

    # Case B: CHECK constraint failure (negative price)
    try:
        cursor.execute("INSERT INTO products VALUES ('SKU-002', -10.00);")
        conn.commit()
    except sqlite3.IntegrityError as err:
        print(f"Caught expected CHECK Constraint Failure: {err}")

    conn.close()


def main():
    demonstrate_sql_injection()
    demonstrate_integrity_error()

if __name__ == "__main__":
    main()
