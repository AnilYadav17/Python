"""
Experiment 03: Data Types, Floating Point, Hashability & Truthiness
===================================================================

Questions Investigated:
-----------------------
1. Why does 0.1 + 0.2 != 0.3, and how does Decimal resolve financial precision?
2. What makes an object hashable, and why do mutable containers fail as keys?
3. What is the memory footprint of range(1_000_000_000)?
4. What non-obvious values are truthy vs falsy?

Instructions to Run:
--------------------
$ python3 26_experiments/03_data_types_experiment.py
"""

from decimal import Decimal
import math
import sys


def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_float_precision_vs_decimal() -> None:
    banner("1. FLOATING POINT PRECISION & DECIMAL")
    float_sum = 0.1 + 0.2
    print(f"0.1 + 0.2 in standard float: {float_sum:.17f}")
    assert float_sum != 0.3, "Standard IEEE 754 float sum should have rounding artifact"
    assert math.isclose(float_sum, 0.3), "math.isclose should recognize them as approximately equal"

    dec_sum = Decimal("0.1") + Decimal("0.2")
    print(f"Decimal('0.1') + Decimal('0.2'): {dec_sum}")
    assert dec_sum == Decimal("0.3"), "Decimal must match exact 0.3"
    print("-> Confirmed: Decimal resolves financial precision issues.")


def test_hashability_rules() -> None:
    banner("2. HASHABILITY RULES FOR KEYS")
    valid_key = (1, 2, "hello")
    print(f"hash({valid_key}): {hash(valid_key)}")

    invalid_tuple = (1, 2, [3, 4])
    is_hashable = False
    try:
        hash(invalid_tuple)
        is_hashable = True
    except TypeError as err:
        print(f"Caught expected TypeError: {err}")

    assert not is_hashable, "Tuple containing list must not be hashable"
    print("-> Confirmed: Tuples are only hashable if all nested items are hashable.")


def test_range_lazy_memory() -> None:
    banner("3. LAZY EVALUATION MEMORY FOOTPRINT")
    range_small = range(10)
    range_huge = range(10_000_000_000)

    size_small = sys.getsizeof(range_small)
    size_huge = sys.getsizeof(range_huge)
    print(f"Size of range(10):              {size_small} bytes")
    print(f"Size of range(10_000_000_000):  {size_huge} bytes")
    assert size_small == size_huge, "Range memory must be O(1) constant regardless of count"

    # Fast O(1) membership test
    assert 9_999_999_998 in range_huge, "O(1) range arithmetic lookup must succeed"
    print("-> Confirmed: Range uses constant O(1) memory and O(1) membership math.")


def test_truthiness_edge_cases() -> None:
    banner("4. TRUTHINESS EDGE CASES")
    assert bool([0]) is True, "List containing 0 is not empty, so it is Truthy!"
    assert bool("0") is True, "String '0' is not empty, so it is Truthy!"
    assert bool("False") is True, "String 'False' is not empty, so it is Truthy!"
    assert bool("") is False, "Empty string is Falsy"
    assert bool([]) is False, "Empty list is Falsy"
    assert bool(None) is False, "None is Falsy"
    print("-> Confirmed: Container truthiness depends on emptiness, not inner zero values.")


def main() -> None:
    test_float_precision_vs_decimal()
    test_hashability_rules()
    test_range_lazy_memory()
    test_truthiness_edge_cases()
    banner("ALL DATA TYPE EXPERIMENTS VERIFIED SUCCESSFULLY")


if __name__ == "__main__":
    main()
