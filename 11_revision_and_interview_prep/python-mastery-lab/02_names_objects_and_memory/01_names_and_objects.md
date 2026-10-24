# Lesson 01: Names and Objects (The Luggage Tag Model)

## 1. The Biggest Mistake Beginners Make
In languages like C, C++, or Java, a variable is taught as a **"box"** that holds data:
```c
int x = 10;  // Creates a box labeled 'x' of size 4 bytes in memory and puts 10 inside it.
```

If you imagine Python variables as "boxes", you will make constant mistakes with lists, functions, and memory.

> **In Python, variables are NOT boxes! Variables are sticky labels (names) attached to objects.**

---

## 2. The Mental Model: Luggage Tags

Think of an airport baggage carousel:
- The **luggage** (the physical suitcase) is the **Object** living in memory.
- The **luggage tag** (with your name written on it) is the **Variable Name**.

```
    Variable Name (Sticky Tag)              Object (In Heap Memory)
   +--------------------------+           +--------------------------+
   |           "a"            | --------> | Integer Object: 100      |
   +--------------------------+           +--------------------------+
```

When you write:
```python
a = 100
b = a
```
You did **NOT** create a second box with the number 100!  
You simply took a second luggage tag named `"b"` and stuck it onto the **same existing suitcase**:

```
   Tag "a" -----\
                 +----> [ Integer Object: 100 ]
   Tag "b" -----/
```

Both `a` and `b` refer to the exact same object in computer memory.

---

## 3. What Does a Python Object Look Like Inside?

Every single object in Python (whether it is an integer, a string, a list, or a function) is an allocated structure called a **`PyObject`**.

At minimum, every `PyObject` has three things:
1. **Type Tag (`ob_type`)**: Tells Python what kind of object this is (e.g., `int`, `str`, `list`).
2. **Reference Count (`ob_refcnt`)**: An integer counter keeping track of how many names or tags are currently pointing to this object.
3. **The Value**: The actual data stored (e.g., the number `100`, or the letters `"hello"`).

```
+----------------------------------------------------+
|               PyObject in RAM Memory               |
|  - Reference Count: 2 (tags 'a' and 'b' point here)|
|  - Type: <class 'int'>                             |
|  - Value: 100                                      |
+----------------------------------------------------+
```

---

## 4. Proving It with `id()`

Python has a built-in function called **`id()`**. It returns the unique memory address of the object.

Let's test our luggage tag model:
```python
a = [10, 20, 30]
b = a

print("Address of a:", id(a))
print("Address of b:", id(b))
print("Do they point to the exact same object?", a is b)
```

**Output:**
```
Address of a: 140238129841280
Address of b: 140238129841280
Do they point to the exact same object? True
```
Because `id(a)` and `id(b)` are identical, `a` and `b` are just two different names for the **one single list**!

---

## 5. Quick Self-Test
1. If you write `x = 5` and then `y = x`, does Python duplicate the number `5` in memory?
   - *Answer: No! `x` and `y` both point to the same integer object `5`.*
2. What are the two core header fields found on every `PyObject` in CPython?
   - *Answer: The reference count (`ob_refcnt`) and the pointer to its type object (`ob_type`).*
