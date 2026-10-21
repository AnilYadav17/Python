"""
03_hash_map_from_scratch.py
Complete pure Python Hash Map implementation from first principles:
- Fixed bucket array
- Hash function with modulo wrapping
- Separate Chaining (linked bucket nodes) for collision resolution
- Dynamic resizing and rehashing when load factor exceeds 0.75
"""

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapFromScratch:
    INITIAL_CAPACITY = 8
    LOAD_FACTOR_THRESHOLD = 0.75

    def __init__(self):
        self.capacity = self.INITIAL_CAPACITY
        self.buckets = [None] * self.capacity
        self.size = 0

    def _hash(self, key) -> int:
        """Computes bucket index for key."""
        return hash(key) % self.capacity

    def put(self, key, value):
        """Inserts or updates key-value pair: O(1) average time."""
        index = self._hash(key)
        head = self.buckets[index]

        # Check if key already exists in the bucket chain -> update
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        # Key does not exist -> insert new node at bucket head (O(1))
        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

        # Check load factor for dynamic resizing
        if (self.size / self.capacity) >= self.LOAD_FACTOR_THRESHOLD:
            self._rehash()

    def get(self, key, default=None):
        """Retrieves value by key: O(1) average time."""
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return default

    def remove(self, key) -> bool:
        """Deletes key from hash map: O(1) average time."""
        index = self._hash(key)
        curr = self.buckets[index]
        prev = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.buckets[index] = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def _rehash(self):
        """Doubles capacity and redistributes all existing entries."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0  # Will be repopulated by put()

        for head in old_buckets:
            curr = head
            while curr:
                self.put(curr.key, curr.value)
                curr = curr.next

    def __len__(self):
        return self.size


def main():
    print("--- Testing Pure Python Hash Map from Scratch ---")
    hmap = HashMapFromScratch()

    # Insert elements
    entries = [
        ("user:101", "Alice"),
        ("user:102", "Bob"),
        ("user:103", "Charlie"),
        ("user:104", "Diana"),
        ("user:105", "Evan"),
        ("user:106", "Fiona"),
        ("user:107", "George")  # Will trigger rehash!
    ]

    for k, v in entries:
        hmap.put(k, v)

    print(f"Hash Map size: {len(hmap)}, Capacity: {hmap.capacity}")
    print(f"Get 'user:101': {hmap.get('user:101')}")
    print(f"Get 'user:105': {hmap.get('user:105')}")
    print(f"Get 'unknown':  {hmap.get('unknown', 'DEFAULT_FALLBACK')}")

    # Test update
    hmap.put("user:101", "Alice_Updated")
    print(f"Updated 'user:101': {hmap.get('user:101')}")

    # Test delete
    hmap.remove("user:102")
    print(f"After deleting 'user:102', lookup: {hmap.get('user:102', 'NOT_FOUND')}")
    print(f"Final size: {len(hmap)}")

if __name__ == "__main__":
    main()
