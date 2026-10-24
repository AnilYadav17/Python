"""
Experiment 10: Advanced Language Features, Typing & Context Managers

Demonstrates:
1. Walrus operator (:=) in filtering loops and comprehensions
2. Extended sequence unpacking (*middle)
3. Custom generator context manager via contextlib
4. Static typing Protocols (runtime duck typing verification)
"""

from contextlib import contextmanager
import time
from typing import Protocol, TypeVar, List


# 1. Walrus Operator in Filtering
def run_walrus_experiment():
    print("=== 1. Walrus Operator Experiment ===")
    raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    # Calculate cube and keep only those greater than 50 in a single pass:
    cubes_over_50 = [cube for n in raw_numbers if (cube := n ** 3) > 50]
    print(f"Numbers cubed > 50: {cubes_over_50}")
    assert cubes_over_50 == [64, 125, 216, 343, 512]


# 2. Extended Unpacking
def run_unpacking_experiment():
    print("\n=== 2. Extended Unpacking Experiment ===")
    data = [10, 20, 30, 40, 50, 60]
    first, *middle, last = data
    print(f"First: {first}, Middle: {middle}, Last: {last}")
    assert first == 10
    assert middle == [20, 30, 40, 50]
    assert last == 60


# 3. Context Manager with contextlib
@contextmanager
def benchmark_timer(name: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = (time.perf_counter() - start) * 1000
        print(f"[{name}] Completed in {elapsed:.3f} ms")


def run_context_experiment():
    print("\n=== 3. Context Manager Experiment ===")
    with benchmark_timer("Sum of Squares"):
        total = sum(x * x for x in range(500_000))
    print(f"Total calculated: {total}")


# 4. Protocols (Structural Subtyping)
class Speaker(Protocol):
    def speak(self) -> str:
        ...


class Dog:
    def speak(self) -> str:
        return "Woof!"


class Robot:
    def speak(self) -> str:
        return "Beep Boop!"


def make_sound(s: Speaker) -> str:
    # Verifies duck typing at runtime
    return s.speak()


def run_protocol_experiment():
    print("\n=== 4. Protocol Duck Typing Experiment ===")
    dog = Dog()
    robot = Robot()
    print(f"Dog says: {make_sound(dog)}")
    print(f"Robot says: {make_sound(robot)}")
    assert make_sound(dog) == "Woof!"
    assert make_sound(robot) == "Beep Boop!"


if __name__ == "__main__":
    run_walrus_experiment()
    run_unpacking_experiment()
    run_context_experiment()
    run_protocol_experiment()
    print("\n[OK] Experiment 10 executed and verified successfully!")
