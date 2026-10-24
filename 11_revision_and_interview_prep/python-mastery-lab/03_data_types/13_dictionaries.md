# Lesson 13: Dictionaries (`dict`) and Hash Tables

## 1. What Is a Dictionary in Simple Words?
A **dictionary** is an ordered collection of **Key-Value pairs**.

Think of a real physical dictionary: you look up a word (the **Key**) and instantly find its definition (the **Value**).

```python
user = {
    "name": "Anil",
    "role": "Engineer",
    "level": 5
}

print(user["name"])  # "Anil"
```

---

## 2. CPython Internals: How Dictionaries Work (Hash Tables)

Dictionaries are Python’s most optimized data structure. Under the hood, Python uses a **Compact Hash Table**:

1. When you insert `user["name"] = "Anil"`, Python calculates `hash("name")`.
2. The hash number determines which slot in an internal array stores the pointer.
3. When you read `user["name"]`, Python hashes `"name"` again and **jumps directly to the memory address in $O(1)$ constant time**!

### The Modern Compact Dict:
Since Python 3.7, dictionaries **guarantee insertion order**. CPython achieves this by separating the hash table into two parts:
- A sparse index table.
- A dense array of `[hash, key_pointer, value_pointer]` entries that preserves the exact order in which you inserted items!

---

## 3. The 4 Essential Dictionary Patterns

### 1. Safe Access with `.get()` (Never Crash on Missing Keys!)
```python
# CRASHES if "age" is missing:
# print(user["age"])  # KeyError: 'age'

# SAFE: returns default value if key doesn't exist:
age = user.get("age", 25)
print("Age is:", age)  # 25
```

### 2. Iterating Over Keys, Values, and Both
```python
stats = {"gold": 100, "silver": 50, "bronze": 10}

for metal, count in stats.items():
    print(f"{metal}: {count}")
```

### 3. Merging Dictionaries with the `|` Operator (Python 3.9+)
```python
defaults = {"theme": "light", "notifications": True}
user_settings = {"theme": "dark"}

# Merge them (user_settings overrides defaults!):
final_config = defaults | user_settings
print(final_config)
# Output: {'theme': 'dark', 'notifications': True}
```

### 4. Grouping with `setdefault()`
```python
word_groups = {}
words = ["apple", "banana", "avocado", "blueberry"]

for word in words:
    first_letter = word[0]
    # If key doesn't exist, create an empty list first:
    word_groups.setdefault(first_letter, []).append(word)

print(word_groups)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}
```

---

## 4. Quick Self-Test
1. What error occurs if you access a non-existent key using bracket notation `my_dict["missing"]`?
   - *Answer: `KeyError` (use `my_dict.get("missing", default)` to avoid crashes).*
2. Do Python dictionaries maintain insertion order?
   - *Answer: Yes, guaranteed since Python 3.7.*
