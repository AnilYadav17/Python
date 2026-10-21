"""
05_advanced_idiomatic.py
Demonstrates advanced database patterns:
Implementing a pure Python Mini-ORM using dataclasses and reflection:
- Maps Python dataclass fields to SQLite columns
- Automatically creates table schemas
- Provides .save() and .find_by() methods
"""

import sqlite3
from dataclasses import dataclass, fields

class Model:
    _conn: sqlite3.Connection = None

    @classmethod
    def set_connection(cls, conn: sqlite3.Connection):
        cls._conn = conn

    @classmethod
    def create_table(cls):
        field_defs = []
        for f in fields(cls):
            sql_type = "TEXT"
            if f.type is int:
                sql_type = "INTEGER"
            elif f.type is float:
                sql_type = "REAL"

            if f.name == "id":
                field_defs.append(f"{f.name} {sql_type} PRIMARY KEY AUTOINCREMENT")
            else:
                field_defs.append(f"{f.name} {sql_type} NOT NULL")

        query = f"CREATE TABLE IF NOT EXISTS {cls.__name__.lower()} ({', '.join(field_defs)});"
        with cls._conn:
            cls._conn.execute(query)

    def save(self):
        model_fields = [f.name for f in fields(self) if f.name != "id"]
        placeholders = ", ".join(["?"] * len(model_fields))
        columns = ", ".join(model_fields)
        values = [getattr(self, f) for f in model_fields]

        query = f"INSERT INTO {self.__class__.__name__.lower()} ({columns}) VALUES ({placeholders});"
        with self._conn:
            cursor = self._conn.execute(query, values)
            object.__setattr__(self, "id", cursor.lastrowid)
        return self

    @classmethod
    def find_all(cls):
        query = f"SELECT * FROM {cls.__name__.lower()};"
        cursor = cls._conn.execute(query)
        field_names = [f.name for f in fields(cls)]
        instances = []
        for row in cursor.fetchall():
            kwargs = dict(zip(field_names, row))
            instances.append(cls(**kwargs))
        return instances


# Domain Model
@dataclass
class Customer(Model):
    name: str
    email: str
    tier: str
    id: int = None


def main():
    print("--- Pure Python Mini-ORM Pattern ---")
    conn = sqlite3.connect(":memory:")
    Model.set_connection(conn)

    # 1. Create table schema from dataclass reflection
    Customer.create_table()

    # 2. Instantiate and persist domain objects
    c1 = Customer(name="Alice Walker", email="alice@corp.com", tier="PLATINUM").save()
    c2 = Customer(name="Bob Vance", email="bob@vance.com", tier="GOLD").save()

    print(f"Persisted Customer 1: ID={c1.id}, Name={c1.name}")
    print(f"Persisted Customer 2: ID={c2.id}, Name={c2.name}")

    # 3. Query all objects
    all_customers = Customer.find_all()
    print(f"\nRetrieved {len(all_customers)} customers from DB:")
    for cust in all_customers:
        print(f"  [{cust.id}] {cust.name} ({cust.tier}) - {cust.email}")

    conn.close()

if __name__ == "__main__":
    main()
