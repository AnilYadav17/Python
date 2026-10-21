"""
01_basic_usage.py
Demonstrates standard library powerhouses:
- os and sys fundamentals
- math calculations
- datetime manipulation
- collections (namedtuple, Counter, defaultdict)
- itertools basics (chain, islice)
"""

import os
import sys
import math
import datetime
from collections import namedtuple, Counter, defaultdict
import itertools

def demonstrate_os_and_sys():
    print("--- 1. os and sys Basics ---")
    current_cwd = os.getcwd()
    print(f"Current Working Directory: {current_cwd}")
    print(f"Python Executable: {sys.executable}")
    print(f"Platform: {sys.platform}")
    print(f"Byte Order: {sys.byteorder}")


def demonstrate_math():
    print("\n--- 2. math Basics ---")
    radius = 5.0
    area = math.pi * math.pow(radius, 2)
    hypot = math.hypot(3.0, 4.0)  # Euclidean distance sqrt(x^2 + y^2)
    print(f"Circle Area (r=5): {area:.2f}")
    print(f"Hypotenuse (3, 4): {hypot}")
    print(f"Is close (0.1 + 0.2, 0.3): {math.isclose(0.1 + 0.2, 0.3)}")


def demonstrate_datetime():
    print("\n--- 3. datetime Basics ---")
    # Timezone-aware UTC timestamp
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    print(f"Current UTC Time: {now_utc.isoformat()}")

    # Timedelta calculation
    two_weeks_later = now_utc + datetime.timedelta(days=14, hours=2)
    print(f"Two weeks later: {two_weeks_later.strftime('%Y-%m-%d %H:%M:%S %Z')}")


def demonstrate_collections():
    print("\n--- 4. collections Basics ---")
    # namedtuple: self-documenting lightweight record
    Point = namedtuple("Point", ["x", "y", "label"])
    p1 = Point(10, 20, "Origin_Offset")
    print(f"Point: {p1}, x={p1.x}, y={p1.y}, label={p1.label}")

    # Counter: multi-set frequency counting
    words = ["python", "go", "python", "rust", "python", "go", "javascript"]
    word_counts = Counter(words)
    print(f"Word counts: {word_counts}")
    print(f"Top 2 most common: {word_counts.most_common(2)}")

    # defaultdict: handles absent keys automatically
    grouped = defaultdict(list)
    for w in words:
        grouped[len(w)].append(w)
    print(f"Grouped by word length: {dict(grouped)}")


def demonstrate_itertools():
    print("\n--- 5. itertools Basics ---")
    list_a = [1, 2, 3]
    list_b = ["a", "b", "c"]

    # itertools.chain: iterates through multiple iterables sequentially without copying
    combined = list(itertools.chain(list_a, list_b))
    print(f"Chained: {combined}")

    # itertools.islice: slices an iterator lazily without building full list
    squared_stream = (x * x for x in itertools.count(1))  # infinite stream
    first_five = list(itertools.islice(squared_stream, 5))
    print(f"First 5 elements from infinite stream: {first_five}")


def main():
    demonstrate_os_and_sys()
    demonstrate_math()
    demonstrate_datetime()
    demonstrate_collections()
    demonstrate_itertools()

if __name__ == "__main__":
    main()
