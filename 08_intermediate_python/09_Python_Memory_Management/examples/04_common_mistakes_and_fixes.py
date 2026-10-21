"""
04_common_mistakes_and_fixes.py
Demonstrates common memory traps and their fixes:
1. The Shallow Copy Trap on nested mutable collections
2. Accidental memory leaks from unmanaged standard dictionaries as caches
"""

import copy

def mistake_1_shallow_copy_trap():
    print("--- 1. Shallow Copy vs Deep Copy Trap ---")
    original_config = {
        "server": "api.prod.com",
        "endpoints": ["/users", "/auth"],  # Nested mutable list
        "limits": {"rate": 100}            # Nested mutable dict
    }

    # SHALLOW COPY: Creates new outer dict, but nested containers share exact same pointers!
    shallow_clone = copy.copy(original_config)
    shallow_clone["endpoints"].append("/billing")
    shallow_clone["limits"]["rate"] = 500

    print("After modifying shallow_clone:")
    print(f"  original_config['endpoints']: {original_config['endpoints']} (Contaminated!)")
    print(f"  original_config['limits']:    {original_config['limits']} (Contaminated!)")

    # FIX: Use copy.deepcopy() to recursively clone all nested structures
    clean_original = {
        "server": "api.prod.com",
        "endpoints": ["/users", "/auth"],
        "limits": {"rate": 100}
    }
    deep_clone = copy.deepcopy(clean_original)
    deep_clone["endpoints"].append("/billing")
    deep_clone["limits"]["rate"] = 500

    print("\nAfter modifying deep_clone:")
    print(f"  clean_original['endpoints']:  {clean_original['endpoints']} (Protected!)")
    print(f"  clean_original['limits']:     {clean_original['limits']} (Protected!)")


def mistake_2_ordinary_dict_cache_leak():
    print("\n--- 2. Ordinary Dict Cache Memory Leak Explanation ---")
    # When using a regular dict: cache[key] = obj
    # The dictionary holds a STRONG reference. The object will NEVER be deallocated
    # as long as the dict lives, even if no other part of the application needs it.
    # Fix: Use collections.OrderedDict with LRU eviction (or functools.lru_cache, or weakref).
    print("Tip: Always bound cache capacities or use weak references to prevent unbounded RAM growth.")


def main():
    mistake_1_shallow_copy_trap()
    mistake_2_ordinary_dict_cache_leak()

if __name__ == "__main__":
    main()
