"""
03_real_world_use_case.py
Real-world scenario: Memory-Safe In-Memory Object Cache using Weak References.
Demonstrates:
- Avoiding cache memory leaks using weakref.WeakValueDictionary
- Objects being automatically evicted from cache when external references drop to zero
"""

import weakref

class HeavyResource:
    """Simulates a heavy dataset or model occupying significant heap memory."""
    def __init__(self, resource_id: str, payload_size: int = 1000):
        self.resource_id = resource_id
        self.data = [0] * payload_size

    def __repr__(self):
        return f"HeavyResource(id={self.resource_id})"


class WeakResourceCache:
    def __init__(self):
        # WeakValueDictionary stores weak references to values
        self._cache = weakref.WeakValueDictionary()

    def get_or_load(self, resource_id: str) -> HeavyResource:
        obj = self._cache.get(resource_id)
        if obj is None:
            print(f"  [Cache MISS] Loading resource '{resource_id}' into memory...")
            obj = HeavyResource(resource_id)
            self._cache[resource_id] = obj
        else:
            print(f"  [Cache HIT] Returning cached instance for '{resource_id}'")
        return obj

    def cached_count(self) -> int:
        return len(self._cache)


def main():
    print("--- Weak Reference Auto-Evicting Cache ---")
    cache = WeakResourceCache()

    # Client A requests resource
    res1 = cache.get_or_load("model_alpha")
    print(f"Cache count: {cache.cached_count()}")

    # Client B requests same resource -> Cache HIT
    res2 = cache.get_or_load("model_alpha")
    print(f"res1 is res2: {res1 is res2}")

    # Client C requests another resource
    res3 = cache.get_or_load("model_beta")
    print(f"Cache count before dropping references: {cache.cached_count()}")

    # Drop external references to model_alpha
    print("\nDropping all external references to 'model_alpha' (res1 and res2)...")
    del res1
    del res2

    # WeakValueDictionary automatically discards dead entries!
    print(f"Cache count after dropping model_alpha: {cache.cached_count()}")
    print(f"Active keys remaining in cache: {list(cache._cache.keys())}")

    # Requesting model_alpha again triggers a cache miss because it was freed
    res1_reloaded = cache.get_or_load("model_alpha")
    print(f"Cache count: {cache.cached_count()}")

if __name__ == "__main__":
    main()
