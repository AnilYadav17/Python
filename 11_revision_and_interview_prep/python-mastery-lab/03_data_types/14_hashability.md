# Lesson 14: Hashability and the Golden Rule of Keys

## 1. What Does "Hashable" Mean in Simple Words?
Have you ever tried using a list as a dictionary key or putting a list inside a set?

```python
d = {}
my_list = [1, 2, 3]
d[my_list] = "secret"
```
**Python Output:**
```
TypeError: unhashable type: 'list'
```
Why does Python refuse to let you use a list as a key?

---

## 2. Why Mutable Objects CANNOT Be Hashed

Dictionaries and sets work by computing a hash number from the key:
`hash(key) -> slot index in memory`.

Imagine if Python allowed lists as dictionary keys:
1. You store `d[[1, 2]] = "data"`. Python calculates `hash([1, 2]) = 987654` and puts it in slot `987654`.
2. Later, you mutate the list: `my_list.append(3)`.
3. Now the list is `[1, 2, 3]`. Its hash changes to `555111`!
4. You try to look up `d[my_list]`. Python looks in slot `555111`, finds nothing, and your data is **lost forever inside the dictionary**!

> **The Golden Rule**: An object can only be a dictionary key or set item if it is **Hashable** (its value never changes during its lifetime).

---

## 3. Which Types Are Hashable?

| Type | Hashable? | Can Be a Dict Key / Set Element? |
| :--- | :--- | :--- |
| `int`, `float`, `bool` | **Yes** | **Yes** |
| `str` | **Yes** | **Yes** |
| `bytes` | **Yes** | **Yes** |
| `tuple` | **Yes** (if all items inside are hashable) | **Yes** |
| `frozenset` | **Yes** | **Yes** |
| `list`, `dict`, `set` | **NO!** (Mutable) | **NO!** (Raises `TypeError`) |

---

## 4. The Tuple Hashability Trap

A tuple is immutable, but what if you put a mutable list inside a tuple?

```python
safe_tuple = (1, 2, "hello")
print("Safe tuple hash:", hash(safe_tuple))  # Works!

tricky_tuple = (1, 2, [3, 4])
print(hash(tricky_tuple))
# CRASH! TypeError: unhashable type: 'list'
```
A tuple is only hashable if **every single item inside it is also hashable**.

---

## 5. Quick Self-Test
1. Can you use `(1, 2, 3)` as a dictionary key?
   - *Answer: Yes, because tuples containing only numbers/strings are immutable and hashable.*
2. Can you use `(1, [2, 3])` as a dictionary key?
   - *Answer: No, because the inner list is mutable, making the entire tuple unhashable.*
