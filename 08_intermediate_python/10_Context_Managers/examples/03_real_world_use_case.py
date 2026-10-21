"""
03_real_world_use_case.py
Real-world scenario: Transactional Unit of Work for Database Sessions.
Demonstrates:
- Automatic transaction commit on success
- Automatic transaction rollback on exception
- Resource release guarantee in both cases
"""

class MockDatabaseConnection:
    def __init__(self):
        self.state = "IDLE"
        self.staged_operations = []

    def begin(self):
        self.state = "IN_TRANSACTION"
        self.staged_operations.clear()
        print("  [DB] Transaction started (BEGIN).")

    def execute(self, sql_stmt):
        if self.state != "IN_TRANSACTION":
            raise RuntimeError("Cannot execute SQL outside an active transaction!")
        self.staged_operations.append(sql_stmt)
        print(f"  [DB] Staged: '{sql_stmt}'")

    def commit(self):
        self.state = "COMMITTED"
        print(f"  [DB] Successfully committed {len(self.staged_operations)} operations (COMMIT).")

    def rollback(self):
        self.state = "ROLLED_BACK"
        print(f"  [DB] Transaction rolled back! Discarded {len(self.staged_operations)} operations (ROLLBACK).")

    def close(self):
        self.state = "CLOSED"
        print("  [DB] Connection returned to connection pool.")


class DatabaseTransaction:
    def __init__(self, connection: MockDatabaseConnection):
        self.conn = connection

    def __enter__(self):
        self.conn.begin()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                # No exception occurred in the block -> commit changes
                self.conn.commit()
            else:
                # Exception occurred -> rollback to maintain ACID atomicity
                print(f"  [Transaction Manager] Exception detected ({exc_type.__name__}: {exc_val}). Rolling back...")
                self.conn.rollback()
        finally:
            # Always close/return connection to pool
            self.conn.close()
        return False  # Propagate exception to caller


def main():
    db = MockDatabaseConnection()

    print("--- Scenario 1: Successful Order Placement ---")
    with DatabaseTransaction(db) as conn:
        conn.execute("INSERT INTO orders (id, user_id, amount) VALUES (101, 42, 99.50)")
        conn.execute("UPDATE accounts SET balance = balance - 99.50 WHERE user_id = 42")
    print(f"Final DB state: {db.state}")

    print("\n--- Scenario 2: Failed Transaction with Automatic Rollback ---")
    try:
        with DatabaseTransaction(db) as conn:
            conn.execute("INSERT INTO inventory (item_id, qty) VALUES ('sku_99', 5)")
            # Simulate a constraint violation mid-transaction
            raise ValueError("Negative stock constraint violation!")
    except ValueError as err:
        print(f"Application caught transaction error: {err}")
    print(f"Final DB state: {db.state}")

if __name__ == "__main__":
    main()
