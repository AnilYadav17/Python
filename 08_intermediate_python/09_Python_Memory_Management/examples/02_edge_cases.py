"""
02_edge_cases.py
Demonstrates memory management edge cases:
- Circular reference cycles defeating standard reference counting
- Detecting and collecting reference cycles with the gc module
- Inspecting GC generational statistics
"""

import gc
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

    def __repr__(self):
        return f"Node({self.name})"


def demonstrate_circular_reference_collection():
    print("--- 1. Circular References and Cyclic Garbage Collector ---")
    # Disable automatic GC so we can inspect cycle manually
    gc.disable()

    # Create two nodes with a mutual circular reference
    node_a = Node("A")
    node_b = Node("B")
    node_a.partner = node_b
    node_b.partner = node_a

    print(f"node_a ref count: {sys.getrefcount(node_a) - 1}")  # 2 (node_a var + node_b.partner)
    print(f"node_b ref count: {sys.getrefcount(node_b) - 1}")  # 2 (node_b var + node_a.partner)

    # Delete external variable references
    del node_a
    del node_b

    # At this point, node_a and node_b are unreachable from user code,
    # but their ref counts remain 1 due to the cycle! Reference counting CANNOT free them.
    print("External variable references deleted. Cycle remains trapped in heap.")

    # Trigger manual cyclic GC collection
    unreachable_count = gc.collect()
    print(f"gc.collect() successfully identified and freed {unreachable_count} circular objects!")

    # Re-enable GC
    gc.enable()


def demonstrate_gc_statistics():
    print("\n--- 2. GC Generational Statistics ---")
    print(f"GC Enabled: {gc.isenabled()}")
    print(f"GC Thresholds (Gen 0, 1, 2): {gc.get_threshold()}")
    stats = gc.get_stats()
    for gen_idx, gen_data in enumerate(stats):
        print(f"  Generation {gen_idx}: collections={gen_data['collections']}, collected={gen_data['collected']}")


def main():
    demonstrate_circular_reference_collection()
    demonstrate_gc_statistics()

if __name__ == "__main__":
    main()
