# Find The Bug: 5 Classic Python Traps

Can you identify the subtle bug in each of these real-world code snippets?

---

## Bug #1: The Vanishing Default Argument
```python
def append_event(event_name: str, event_log: list = []):
    event_log.append(event_name)
    return event_log

print(append_event("User Registered"))
print(append_event("Payment Succeeded"))
```
**Symptoms**: The second call returns `['User Registered', 'Payment Succeeded']`!  
**Why**: Default arguments evaluate **once** when the function definition is executed, not each time the function is called! All callers share the single list instance.  
**Fix**: Use `event_log: list | None = None` and initialize `if event_log is None: event_log = []`.

---

## Bug #2: The Modifying Iteration Trap
```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)
```
**Symptoms**: `numbers` becomes `[1, 3, 5, 6]` — `6` is still in the list!  
**Why**: Modifying a list while iterating over it shifts index positions. When index 1 (`2`) is removed, index 2 (`4`) shifts to index 1 and the loop skips ahead!  
**Fix**: Iterate over a copy (`for num in numbers[:]:`) or use a list comprehension `numbers = [n for n in numbers if n % 2 != 0]`.

---

## Bug #3: The Shadowing Exception Trap
```python
def check_connection():
    try:
        raise ConnectionResetError("Connection dropped by peer")
    finally:
        return "Cleaned up"

print(check_connection())
```
**Symptoms**: The function prints `"Cleaned up"` and the `ConnectionResetError` is completely lost without a trace!  
**Why**: A `return` or `break` statement inside a `finally` block **silently swallows any active unhandled exception**!  
**Fix**: Never put a `return` statement inside a `finally` block unless you intentionally want to suppress exceptions.

---

## Bug #4: The Tuple Mutation Illusion
```python
data = (10, [20, 30])
try:
    data[1] += [40]
except TypeError:
    print("Caught TypeError!")

print(data)
```
**Symptoms**: It prints `"Caught TypeError!"`, BUT `data` is now `(10, [20, 30, 40])`!  
**Why**: The `+=` operator on a list mutates the list in-place first, and then attempts to assign the mutated list back to `data[1]`. The assignment to a tuple element triggers `TypeError`, but the list in memory was already mutated!

---

## Bug #5: Is vs Equal on Integers
```python
a = 256
b = 256
print(a is b)  # True

x = 1000
y = 1000
print(x is y)  # False in standard REPL!
```
**Why**: CPython caches small integer singletons between `-5` and `256` for memory efficiency. Beyond 256, numbers are new heap objects unless folded by the compiler. Always use `==` for value comparison, never `is`!
