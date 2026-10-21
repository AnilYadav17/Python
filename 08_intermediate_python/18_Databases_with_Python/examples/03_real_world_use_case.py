"""
03_real_world_use_case.py
Real-world scenario: E-commerce Atomic Transaction Engine.
Demonstrates:
- ACID Transaction Management: Atomicity across customer balance, inventory, and orders
- Automatic commit on clean execution
- Automatic rollback on inventory shortfall or payment failure
"""

import sqlite3

class OrderProcessingEngine:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def setup_schema(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE inventory (
                    sku TEXT PRIMARY KEY,
                    item_name TEXT NOT NULL,
                    stock INTEGER NOT NULL CHECK(stock >= 0)
                );
            """)
            self.conn.execute("""
                CREATE TABLE customers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    balance REAL NOT NULL CHECK(balance >= 0)
                );
            """)
            self.conn.execute("""
                CREATE TABLE orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    sku TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    total_price REAL NOT NULL
                );
            """)
            # Populate initial data
            self.conn.execute("INSERT INTO inventory VALUES ('PHONE-01', 'Smartphone', 2);")
            self.conn.execute("INSERT INTO customers VALUES (1, 'Alice', 1000.0);")

    def process_order(self, customer_id: int, sku: str, quantity: int, unit_price: float):
        total_price = quantity * unit_price
        cursor = self.conn.cursor()

        # Using connection as context manager automatically manages transaction (BEGIN, COMMIT, ROLLBACK)
        try:
            with self.conn:
                print(f"\n[Transaction Begin] Customer {customer_id} ordering {quantity}x {sku} (${total_price:.2f})...")

                # Step 1: Check and decrement stock (CHECK constraint triggers error if stock < 0)
                cursor.execute(
                    "UPDATE inventory SET stock = stock - ? WHERE sku = ?;",
                    (quantity, sku)
                )

                # Step 2: Debit customer balance (CHECK constraint triggers error if balance < 0)
                cursor.execute(
                    "UPDATE customers SET balance = balance - ? WHERE id = ?;",
                    (total_price, customer_id)
                )

                # Step 3: Insert order record
                cursor.execute(
                    "INSERT INTO orders (customer_id, sku, quantity, total_price) VALUES (?, ?, ?, ?);",
                    (customer_id, sku, quantity, total_price)
                )
            print("  -> Transaction SUCCESS! All changes committed atomically.")
            return True
        except sqlite3.IntegrityError as err:
            print(f"  -> Transaction FAILED ({err}). Rolled back all changes!")
            return False


def main():
    conn = sqlite3.connect(":memory:")
    engine = OrderProcessingEngine(conn)
    engine.setup_schema()

    # Order 1: Buy 1 phone for $400 (Succeeds)
    engine.process_order(customer_id=1, sku="PHONE-01", quantity=1, unit_price=400.0)

    # Order 2: Buy 5 phones (Fails: inventory stock is only 1 left -> triggers rollback!)
    engine.process_order(customer_id=1, sku="PHONE-01", quantity=5, unit_price=400.0)

    # Verify state: Stock should be exactly 1, Balance should be $600
    cursor = conn.cursor()
    cursor.execute("SELECT stock FROM inventory WHERE sku = 'PHONE-01';")
    stock = cursor.fetchone()[0]
    cursor.execute("SELECT balance FROM customers WHERE id = 1;")
    balance = cursor.fetchone()[0]

    print(f"\nFinal State after rollback:")
    print(f"  Remaining Stock: {stock} (Preserved!)")
    print(f"  Remaining Balance: ${balance:.2f} (Preserved!)")
    conn.close()

if __name__ == "__main__":
    main()
