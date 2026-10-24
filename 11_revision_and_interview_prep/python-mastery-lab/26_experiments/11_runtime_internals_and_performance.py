"""
Experiment 11: CPython Internals, Profiling & Memory Optimization

Demonstrates:
1. Bytecode disassembly via dis module
2. Memory footprint comparison: __slots__ vs standard __dict__
3. Safe SQLite transactions with rollback on failure
"""

import dis
import sqlite3
import sys
import tracemalloc


# 1. Bytecode Disassembly
def sample_math(x, y):
    return (x + y) * 2


def run_bytecode_experiment():
    print("=== 1. Bytecode Disassembly Experiment ===")
    print("Function source: (x + y) * 2")
    print("Disassembled CPython Opcodes:")
    dis.dis(sample_math)


# 2. __slots__ Memory Benchmarking
class StandardItem:
    def __init__(self, item_id: int, name: str):
        self.item_id = item_id
        self.name = name


class SlottedItem:
    __slots__ = ("item_id", "name")
    def __init__(self, item_id: int, name: str):
        self.item_id = item_id
        self.name = name


def run_memory_benchmark():
    print("\n=== 2. Memory Benchmark: __slots__ vs __dict__ ===")
    count = 100_000

    tracemalloc.start()
    standard_objects = [StandardItem(i, f"Item_{i}") for i in range(count)]
    current, peak_standard = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    del standard_objects

    tracemalloc.start()
    slotted_objects = [SlottedItem(i, f"Item_{i}") for i in range(count)]
    current, peak_slotted = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    del slotted_objects

    print(f"RAM for {count:,} Standard Objects (__dict__): {peak_standard / 1024 / 1024:.2f} MB")
    print(f"RAM for {count:,} Slotted Objects  (__slots__): {peak_slotted / 1024 / 1024:.2f} MB")
    savings = (1 - (peak_slotted / peak_standard)) * 100
    print(f"Memory Saved by __slots__: {savings:.1f}%")
    assert peak_slotted < peak_standard


# 3. SQLite ACID Transaction Rollback
def run_sqlite_transaction_experiment():
    print("\n=== 3. SQLite Transaction & Rollback Experiment ===")
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE accounts (name TEXT, balance INTEGER)")
        conn.execute("INSERT INTO accounts VALUES ('Alice', 1000), ('Bob', 500)")

    # Test rollback on error
    try:
        with conn:
            conn.execute("UPDATE accounts SET balance = balance - 200 WHERE name = 'Alice'")
            # Intentionally simulate an unexpected crash during money transfer:
            raise RuntimeError("Database connection interrupted during transfer!")
            conn.execute("UPDATE accounts SET balance = balance + 200 WHERE name = 'Bob'")
    except RuntimeError:
        print("Caught simulated crash! Verifying database was rolled back...")

    cursor = conn.execute("SELECT name, balance FROM accounts")
    rows = dict(cursor.fetchall())
    print("Account balances after rollback:", rows)
    # Alice's balance must remain 1000, not 800!
    assert rows["Alice"] == 1000
    assert rows["Bob"] == 500
    print("ACID Rollback confirmed successful!")
    conn.close()


if __name__ == "__main__":
    run_bytecode_experiment()
    run_memory_benchmark()
    run_sqlite_transaction_experiment()
    print("\n[OK] Experiment 11 executed and verified successfully!")
