"""
01_basic_usage.py
Demonstrates empirical execution scaling across standard Big-O complexity classes:
- O(1) Constant Time
- O(log n) Logarithmic Time
- O(n) Linear Time
- O(n log n) Linearithmic Time
- O(n^2) Quadratic Time
"""

import time
import bisect

def time_function(func, *args):
    start = time.perf_counter()
    func(*args)
    return (time.perf_counter() - start) * 1000  # ms


# 1. O(1) Constant Time
def operation_o_one(data, index):
    return data[index]


# 2. O(log n) Logarithmic Time
def operation_o_log_n(sorted_data, target):
    return bisect.bisect_left(sorted_data, target)


# 3. O(n) Linear Time
def operation_o_n(data):
    total = 0
    for x in data:
        total += x
    return total


# 4. O(n log n) Linearithmic Time
def operation_o_n_log_n(data):
    return sorted(data)


# 5. O(n^2) Quadratic Time
def operation_o_n_squared(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] == data[j]:
                count += 1
    return count


def main():
    print("--- Empirical Big-O Scaling Demonstration ---")
    sizes = [1000, 5000]

    for n in sizes:
        raw_list = list(range(n, 0, -1))
        sorted_list = list(range(n))

        t_o1 = time_function(operation_o_one, raw_list, n // 2)
        t_logn = time_function(operation_o_log_n, sorted_list, n // 2)
        t_n = time_function(operation_o_n, raw_list)
        t_nlogn = time_function(operation_o_n_log_n, raw_list)
        t_n2 = time_function(operation_o_n_squared, raw_list[:min(n, 3000)])  # Cap to prevent long runs

        print(f"\n[Dataset Size: N = {n}]")
        print(f"  O(1)       dict/list index:  {t_o1:>8.4f} ms")
        print(f"  O(log n)   binary search:    {t_logn:>8.4f} ms")
        print(f"  O(n)       linear scan:      {t_n:>8.4f} ms")
        print(f"  O(n log n) timsort:          {t_nlogn:>8.4f} ms")
        if n <= 3000:
            print(f"  O(n^2)     nested loop:      {t_n2:>8.4f} ms")
        else:
            print(f"  O(n^2)     nested loop (scaled 3k): {t_n2:>8.4f} ms")

if __name__ == "__main__":
    main()
