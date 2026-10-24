"""
Enterprise Database Application with Repository Pattern & Migrations (Project 08)

Features:
- Schema migration manager with migration history tracking
- Repository Pattern separating domain entities from raw SQL
- Parameterized queries (?) preventing all SQL injection vectors
- Unit-of-Work pattern for ACID atomic multi-step transactions
"""

from dataclasses import dataclass
from pathlib import Path
import sqlite3
from typing import List, Optional


@dataclass
class Product:
    id: Optional[int]
    sku: str
    name: str
    price: float
    stock_quantity: int


class MigrationManager:
    """Tracks and executes incremental database schema migrations."""

    MIGRATIONS = [
        # Version 1: Initial schema
        (1, """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version INTEGER PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK(price >= 0),
                stock_quantity INTEGER NOT NULL CHECK(stock_quantity >= 0)
            );
        """),
        # Version 2: Index for ultra-fast SKU lookups
        (2, """
            CREATE INDEX IF NOT EXISTS idx_products_sku ON products(sku);
        """)
    ]

    @classmethod
    def apply_migrations(cls, conn: sqlite3.Connection) -> int:
        """Apply all pending migrations. Returns count of applied migrations."""
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS schema_migrations (
                    version INTEGER PRIMARY KEY,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

        cursor = conn.execute("SELECT version FROM schema_migrations")
        applied_versions = {row[0] for row in cursor.fetchall()}

        applied_count = 0
        for version, script in cls.MIGRATIONS:
            if version not in applied_versions:
                with conn:
                    conn.executescript(script)
                    conn.execute("INSERT INTO schema_migrations (version) VALUES (?)", (version,))
                applied_count += 1

        return applied_count


class ProductRepository:
    """Data Access Object for Product domain entities."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create(self, product: Product) -> Product:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO products (sku, name, price, stock_quantity) VALUES (?, ?, ?, ?)",
                (product.sku, product.name, product.price, product.stock_quantity)
            )
            product.id = cursor.lastrowid
            return product

    def find_by_sku(self, sku: str) -> Optional[Product]:
        cursor = self.conn.execute(
            "SELECT id, sku, name, price, stock_quantity FROM products WHERE sku = ?",
            (sku,)
        )
        row = cursor.fetchone()
        if row:
            return Product(id=row[0], sku=row[1], name=row[2], price=row[3], stock_quantity=row[4])
        return None

    def update_stock(self, product_id: int, delta: int) -> bool:
        """Atomically update stock. Returns True if updated, False if insufficient stock."""
        cursor = self.conn.execute(
            "UPDATE products SET stock_quantity = stock_quantity + ? WHERE id = ? AND stock_quantity + ? >= 0",
            (delta, product_id, delta)
        )
        return cursor.rowcount > 0

    def list_all(self) -> List[Product]:
        cursor = self.conn.execute("SELECT id, sku, name, price, stock_quantity FROM products ORDER BY name ASC")
        return [Product(*row) for row in cursor.fetchall()]


class UnitOfWork:
    """Context manager controlling atomic transactional business operations."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.products = ProductRepository(conn)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
            return False  # Propagate exception
        else:
            self.conn.commit()
            return True
