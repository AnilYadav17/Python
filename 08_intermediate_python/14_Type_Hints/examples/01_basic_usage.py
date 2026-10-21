"""
01_basic_usage.py
Demonstrates foundational type annotations in Python:
- Variable and function type hints
- Built-in generics (list, dict, set, tuple)
- Union types (X | Y) and Optional types (T | None)
- Introspecting __annotations__
"""

from typing import Optional, Union

# 1. Variable Type Hints
app_version: str = "2.4.1"
max_connections: int = 100
is_production: bool = True

# 2. Modern Built-in Generic Collections (Python 3.9+)
active_ips: list[str] = ["192.168.1.1", "10.0.0.1"]
status_codes: set[int] = {200, 201, 204}
user_lookup: dict[str, int] = {"alice": 101, "bob": 102}

# Fixed-length heterogeneous tuple vs arbitrary-length homogeneous tuple
server_endpoint: tuple[str, int] = ("127.0.0.1", 8080)
raw_measurements: tuple[float, ...] = (1.2, 4.5, 9.8, 12.3)

# 3. Modern Union and Optional Syntax (Python 3.10+)
def calculate_discount(price: float, coupon_code: str | None = None) -> float:
    """Computes price after applying optional coupon code."""
    if coupon_code == "SAVE20":
        return round(price * 0.80, 2)
    return price


def parse_numeric_id(raw_value: int | str) -> int:
    """Accepts union of int or str and normalizes to int."""
    if isinstance(raw_value, str):
        return int(raw_value.strip())
    return raw_value


def main():
    print("--- 1. Testing Annotated Functions ---")
    base_price = 100.0
    discounted = calculate_discount(base_price, "SAVE20")
    print(f"Base: ${base_price:.2f}, Discounted: ${discounted:.2f}")

    user_id_1 = parse_numeric_id("  4042  ")
    user_id_2 = parse_numeric_id(5050)
    print(f"Parsed IDs: {user_id_1}, {user_id_2}")

    print("\n--- 2. Inspecting Function Annotations ---")
    print("calculate_discount annotations:")
    for param, type_obj in calculate_discount.__annotations__.items():
        print(f"  {param:<12} -> {type_obj}")

if __name__ == "__main__":
    main()
