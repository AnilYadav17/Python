# Lesson 01: Iterables vs. Iterators (The Book Analogy)

## 1. What Is This in Simple Words?
Many programmers use the words "iterable" and "iterator" interchangeably, but in Python they are two very different things!

> **The Book & Bookmark Analogy**:
> - An **Iterable** is a physical book on a shelf. It contains pages, but it doesn't remember what page you are currently reading.
> - An **Iterator** is a bookmark. It marks your current position and moves to the next page when you ask for it.

---

## 2. Technical Definitions

1. **Iterable**:
   - Any object that can return its members one at a time.
   - Examples: `list`, `str`, `tuple`, `dict`, `set`.
   - **How to identify one**: It implements the **`__iter__()`** method.
   - You can pass it to `iter(my_obj)` to get an iterator.

2. **Iterator**:
   - The actual stateful stream object that yields items one by one.
   - **How to identify one**: It implements **both `__iter__()` AND `__next__()`**!
   - Every time you call `next(my_iterator)`, it hands you the next item.
   - When no items remain, it raises a **`StopIteration`** exception.

---

## 3. Watching the Iterator Protocol in Action

When you write a simple `for` loop:
```python
for item in [10, 20, 30]:
    print(item)
```

Here is the exact code Python runs behind the scenes:
```python
# Step 1: Python gets an iterator from the list:
iterator = iter([10, 20, 30])  # Calls [10, 20, 30].__iter__()

# Step 2: Python repeatedly calls next() in a loop:
while True:
    try:
        item = next(iterator)  # Calls iterator.__next__()
        print(item)
    except StopIteration:
        # Step 3: When items run out, StopIteration signals the end!
        break
```

---

## 4. Fascinating Fact 💡
> **Did you know?**
> A list is an iterable, but a list is **NOT** an iterator!  
> If you call `next([1, 2, 3])`, Python will crash with:
> `TypeError: 'list' object is not an iterator`.  
> A list doesn't track a reading position—it creates a separate iterator object (`list_iterator`) each time you loop over it so multiple loops can read the list independently at the same time!

---

## 5. Once an Iterator Is Exhausted, It Is Dead!

A list can be looped over 100 times.  
An **iterator can only be consumed ONCE**:

```python
nums = [1, 2, 3]
it = iter(nums)

# First pass consumes all items:
print(list(it))  # [1, 2, 3]

# Second pass: the iterator is exhausted!
print(list(it))  # [] (Empty!)
```

---

## 6. Quick Self-Test
1. What two dunder methods must an object implement to be a true Iterator?
   - *Answer: `__iter__()` and `__next__()`.*
2. What exception signals that an iterator has no more elements?
   - *Answer: `StopIteration`.*
