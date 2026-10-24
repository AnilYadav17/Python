# Lesson 09: Basic Input and Output (I/O)

## 1. Output with `print()`

The `print()` function is the first function everyone learns in Python. But underneath its simple surface, it has 4 powerful options:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### 1. `sep`: Change what goes BETWEEN items
By default, Python separates items with a single space:
```python
print("2026", "10", "24")
# Output: 2026 10 24

# Change the separator to a hyphen:
print("2026", "10", "24", sep="-")
# Output: 2026-10-24
```

### 2. `end`: Change what goes at the END of the line
By default, `print()` adds a newline (`\n`), moving the cursor to the next line. You can change this so output stays on the same line:
```python
print("Loading", end="...")
print("Done!")
# Output: Loading...Done!
```

### 3. `flush=True`: Force output to appear instantly
Python normally buffers output (saving it up in memory before printing to the screen in batches). If you are building a live countdown timer or progress bar, use `flush=True` so it appears on screen without delay.

---

## 2. Input with `input()`

The `input()` function pauses your program, prompts the user, and waits for them to type something and press Enter:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### The #1 Beginner Trap with `input()`:
> **`input()` ALWAYS returns a string (`str`), NEVER a number!**

```python
# The Trap:
age = input("Enter your age: ")  # User types 25
# age is NOT the number 25. It is the text string "25"!

next_year = age + 1
# CRASH! TypeError: can only concatenate str (not "int") to str
```

### The Fix: Convert the String to an Integer
```python
age_str = input("Enter your age: ")
age = int(age_str)  # Convert text "25" to integer 25
next_year = age + 1
print(f"Next year you will be {next_year}!")
```

---

## 3. Professional Formatting with F-Strings

F-strings (introduced in Python 3.6 and refined in 3.12+) are the fastest and cleanest way to format output:

### 1. Rounding Decimals:
```python
pi = 3.14159265
print(f"Pi to 2 decimal places: {pi:.2f}")
# Output: Pi to 2 decimal places: 3.14
```

### 2. Formatting Large Numbers with Commas:
```python
population = 1428627663
print(f"Population: {population:,}")
# Output: Population: 1,428,627,663
```

### 3. Padding with Zeros:
```python
file_number = 7
print(f"Invoice_{file_number:04d}.pdf")
# Output: Invoice_0007.pdf
```

### 4. Text Alignment (Left, Center, Right):
```python
item = "Coffee"
print(f"{item:<10} | Left aligned (10 spaces)")
print(f"{item:^10} | Centered (10 spaces)")
print(f"{item:>10} | Right aligned (10 spaces)")
```

---

## 4. Quick Self-Test
1. What does `print("A", "B", "C", sep="*", end="!")` output?
   - *Answer: `A*B*C!`*
2. If the user enters `100` at `val = input()`, what is `type(val)`?
   - *Answer: `<class 'str'>` (a string, not an integer).*
