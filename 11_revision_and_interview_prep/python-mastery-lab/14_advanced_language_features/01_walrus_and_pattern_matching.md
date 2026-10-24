# Lesson 14.1: Modern Python Features — The Walrus Operator & Structural Pattern Matching

## 1. What Is This in Simple Words?
Python keeps evolving! Over the last few versions, Python added two superpowers that clean up repetitive code:
1. **The Walrus Operator (`:=`)**: Lets you assign a variable *inside* an expression or condition at the exact moment you check it. It's called the walrus because `:=` looks like two eyes and a pair of tusks!
2. **Structural Pattern Matching (`match / case`)**: A supercharged `switch` statement that can unpack objects, check types, inspect dictionary keys, and test conditions simultaneously.

---

## 2. Superpower #1: The Walrus Operator (`:=`)

### The Old Way vs The Walrus Way
Look at how much cleaner your code becomes:

**Before (Redundant code):**
```python
user_input = input("Enter something: ")
while user_input != "quit":
    print(f"You entered: {user_input}")
    user_input = input("Enter something: ")
```

**After (Clean & Elegant with Walrus):**
```python
# Simulating reading chunks:
data_stream = ["chunk1", "chunk2", "quit"]
iterator = iter(data_stream)

while (chunk := next(iterator)) != "quit":
    print(f"Processing: {chunk}")
```

### In List Comprehensions:
Avoid calculating expensive functions twice:
```python
def expensive_calculation(x):
    return x ** 2 + 10

numbers = [1, 2, 3, 4, 5]
# Calculate result once, store in 'y', and filter/use it immediately:
results = [y for x in numbers if (y := expensive_calculation(x)) > 15]
print(results)  # [19, 26, 35]
```

---

## 3. Superpower #2: Structural Pattern Matching (`match / case`)
Introduced in Python 3.10 (PEP 634), this is not just an ordinary `switch` statement. It inspects the *shape* (structure) of your data.

### Unpacking Tuples and Guard Clauses:
```python
def process_command(command: tuple):
    match command:
        case ("move", x, y):
            print(f"Moving to coordinates ({x}, {y})")
        case ("move", x, y) if x < 0 or y < 0:
            print("Cannot move to negative coordinates!")
        case ("quit",):
            print("Exiting application...")
        case ("alert", str(msg)):
            print(f"ALERT RECEIVED: {msg}")
        case _:
            print("Unknown command format!")

process_command(("move", 10, 20))     # Moving to coordinates (10, 20)
process_command(("alert", "System OK"))# ALERT RECEIVED: System OK
```

### Matching Dictionary Structures:
```python
def handle_event(event: dict):
    match event:
        case {"type": "login", "user": {"id": int(user_id), "admin": True}}:
            print(f"Administrator {user_id} logged in!")
        case {"type": "login", "user": {"id": int(user_id)}}:
            print(f"Standard user {user_id} logged in.")
        case _:
            print("Unrecognized event payload.")
```

---

## 4. Mind-Blowing Facts! 💡

> **Fact 1: The Walrus Controversy!**  
> PEP 572 (which introduced the walrus operator `:=` in Python 3.8) caused so much heated debate and toxic arguing in the Python community that Python's creator, Guido van Rossum, stepped down as the "Benevolent Dictator For Life" (BDFL) of Python in July 2018!
>
> **Fact 2: Pattern Matching Variables Are Bound!**  
> In `case ("move", x, y):`, `x` and `y` are real local variables! If the pattern matches, `x` and `y` remain accessible even *after* the `match` block ends!

---

## 5. Quick Self-Test
1. **Question**: Can you use `=` instead of `:=` inside an `if` statement condition in Python?
   - *Answer*: No! In Python, `if x = 5:` is an immediate `SyntaxError`. The standard `=` is purely a statement, not an expression. Only `:=` returns the assigned value.
2. **Exercise**: Predict the output:
```python
if (n := len("Python")) > 3:
    print(f"Length is {n}")
```
*(Answer: Length is 6)*
