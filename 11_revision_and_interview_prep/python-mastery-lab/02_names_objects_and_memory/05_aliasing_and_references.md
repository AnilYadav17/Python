# Lesson 05: Aliasing, References, and Function Calls

## 1. What Is Aliasing?
**Aliasing** happens when two or more variables refer to the exact same object in memory.

If that object is **mutable** (like a list or a dictionary), modifying it through *one* name will secretly change what you see through *all other* names!

```python
original_scores = [90, 85, 78]
backup_scores = original_scores  # Aliasing! Both point to the same list.

# Add a bonus score through backup_scores:
backup_scores.append(100)

print("Original Scores:", original_scores)
# Output: [90, 85, 78, 100]  <- Surprised? It modified original_scores too!
```

---

## 2. The Famous Matrix Multiplier Trap: `[[0] * 3] * 3`

Look at this very common mistake when trying to create a 3x3 grid of zeros:

```python
# Create a 3x3 grid:
grid = [[0] * 3] * 3
print("Grid:", grid)
# Looks innocent: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Now, change row 0, column 0 to 99:
grid[0][0] = 99

print("Grid after change:")
print(grid)
```

**Output:**
```
[[99, 0, 0], [99, 0, 0], [99, 0, 0]]
```
Every single row changed to `99`! Why?  
Because `[ [0]*3 ] * 3` did **not** make three separate rows. It made **one single row** and duplicated the pointer three times!

```
         grid[0] -----\
         grid[1] -----> [ 99, 0, 0 ]
         grid[2] -----/
```

### The Correct Way to Build a Matrix:
Use a **list comprehension** so each row is a newly allocated object:
```python
grid = [[0 for _ in range(3)] for _ in range(3)]
grid[0][0] = 99
print(grid)
# Correct: [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 3. How Python Passes Arguments to Functions

Is Python "Pass-by-Value" or "Pass-by-Reference"?

> **The True Answer: Python is "Pass-by-Object-Reference" (also called Call-by-Sharing).**

When you pass an argument to a function:
1. Python passes a pointer to the existing object.
2. The function's parameter name becomes an alias for that object.

### Case A: Passing an Immutable Object (Numbers, Strings)
The function CANNOT change the caller's value:
```python
def add_five(num):
    num = num + 5  # Rebinds local name 'num' to a new integer
    print("Inside function:", num)

val = 10
add_five(val)
print("Outside function:", val)
```
**Output:**
```
Inside function: 15
Outside function: 10   <- Completely unchanged!
```

### Case B: Passing a Mutable Object (Lists, Dictionaries)
If the function modifies the object in-place, the caller **WILL** see the change!
```python
def add_item(shopping_list):
    shopping_list.append("Milk")  # In-place mutation!

cart = ["Eggs", "Bread"]
add_item(cart)
print("Cart outside:", cart)
# Output: ['Eggs', 'Bread', 'Milk']  <- Changed!
```

---

## 4. Quick Self-Test
1. In `a = [1, 2]`, `b = a`, `b.append(3)`, what is `a`?
   - *Answer: `[1, 2, 3]` because `a` and `b` are aliases pointing to the same list.*
2. How do you prevent a function from accidentally mutating your original list?
   - *Answer: Pass a shallow copy of the list: `add_item(cart.copy())` or `add_item(cart[:])`.*
