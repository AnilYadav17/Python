# Lesson 04: Literals and Notation

## 1. What Is a Literal in Simple Words?
A **literal** is any raw, fixed value written directly into your code. 

For example, in `age = 25`:
- `age` is the variable name (an identifier).
- `25` is the literal value.

Python has literals for numbers, text, booleans, and collections.

---

## 2. Numeric Literals

### 1. Integer Literals (Whole Numbers)
```python
x = 42            # Standard decimal (base 10)
big_num = 1_000_000  # You can use underscores like commas! 1_000_000 is 1000000.
```

Python also lets you write numbers in other number bases:
- **Binary (base 2)**: Starts with `0b` $\to$ `0b1010` (which is decimal `10`).
- **Octal (base 8)**: Starts with `0o` $\to$ `0o12` (which is decimal `10`).
- **Hexadecimal (base 16)**: Starts with `0x` $\to$ `0xFF` (which is decimal `255`).

### 2. Floating-Point Literals (Decimals)
```python
price = 19.99
rate = .5          # Valid, same as 0.5
scientific = 1.5e3 # 1.5 * 10^3 = 1500.0
tiny = 2.5e-4      # 2.5 * 10^-4 = 0.00025
```

### 3. Complex Literals
Python natively supports complex numbers! In engineering and math, $\sqrt{-1}$ is written as $i$, but Python uses **`j`**:
```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
```

---

## 3. String Literals (Text)

You can write strings in multiple ways:

1. **Single vs Double Quotes**:
   ```python
   name = 'Alice'
   message = "Hello, world!"
   # Double quotes make it easy to include single quotes:
   quote = "It's a sunny day."
   ```

2. **Triple Quotes (Multi-line text)**:
   ```python
   essay = """This is line 1.
   This is line 2.
   All formatting and newlines are preserved exactly."""
   ```

3. **Raw Strings (`r"..."`)**:
   In standard strings, `\n` means a newline and `\t` means a tab. But if you put an `r` in front, Python treats backslashes literally:
   ```python
   normal_path = "C:\new_folder\test"   # \n creates an unwanted newline!
   raw_path = r"C:\new_folder\test"      # Keeps \n as two literal characters '\' and 'n'
   ```

4. **Formatted Strings / F-Strings (`f"..."`)**:
   Put an `f` in front to easily inject variables into text:
   ```python
   user = "Anil"
   score = 98
   print(f"Welcome {user}! Your score is {score}.")
   ```

---

## 4. Special Literals

- **Boolean**: `True` and `False` (always capitalized).
- **None**: `None` represents the absence of a value (equivalent to `null` or `nil` in other languages).

---

## 5. Quick Self-Test
1. What does `1_000_000` evaluate to in Python?
   - *Answer: The integer `1000000`. The underscores are purely visual for humans to read large numbers easily.*
2. Why is `r"C:\users\anil\notes"` preferred over `"C:\users\anil\notes"` when writing Windows paths?
   - *Answer: Because `\n` in a regular string is converted into a newline character, breaking the file path. The `r` prefix makes it a raw string.*
