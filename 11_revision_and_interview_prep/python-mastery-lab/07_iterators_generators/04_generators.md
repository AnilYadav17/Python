# Lesson 04: Generators and `yield` (Freezing Functions in Time)

## 1. What Is a Generator in Simple Words?
A standard function runs from top to bottom, hits `return`, and completely disappears from memory.

A **Generator** is a magical function that **can pause execution in the middle, return a value, and freeze in time until you ask it for the next value!**

You create a generator by simply using the keyword **`yield`** instead of `return`.

---

## 2. Minimal Example: A Pausing Counter

```python
def count_up_to(max_num):
    print("Function starting...")
    count = 1
    while count <= max_num:
        print(f"Pausing before yielding {count}...")
        yield count  # Pauses right here and gives 'count' to caller!
        print(f"Resuming after yielding {count}...")
        count += 1
    print("Function finished!")
```

### Let's Step Through It Manually:
```python
# Calling the generator function DOES NOT run the code!
# It creates a Generator Object:
gen = count_up_to(2)
print("Generator created:", gen)

# Now, we pull values with next():
print("First pull: ", next(gen))
print("Second pull:", next(gen))
```

**Output:**
```
Generator created: <generator object count_up_to at 0x7f...>
Function starting...
Pausing before yielding 1...
First pull:  1
Resuming after yielding 1...
Pausing before yielding 2...
Second pull: 2
```

---

## 3. Fascinating Fact 💡
> **Did you know?**
> How does Python freeze a generator in RAM?  
> When a normal function runs, its execution frame lives on the C call stack and gets destroyed when the function returns.  
> But when Python compiles a function with `yield`, it marks it with the `CO_GENERATOR` flag. Its **`PyFrameObject` is allocated on the Heap**! Python literally stores the instruction pointer and all local variables frozen in memory so it can jump back in seamlessly on the next `next()` call!

---

## 4. Processing 100 Gigabytes of Data with 5 Megabytes of RAM!

Imagine you have a server log file that is 50 Gigabytes on disk.
If you do this:
```python
# DISASTER: Reads entire 50GB into RAM at once -> Computer crashes with MemoryError!
with open("huge_server.log") as f:
    lines = f.readlines()
```

With a Generator pipeline:
```python
def read_huge_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # Yields ONE single line at a time!
            yield line.strip()

# Memory usage is practically ZERO (~5 KB) because only 1 line exists in RAM at a time!
for line in read_huge_file("huge_server.log"):
    if "ERROR" in line:
        send_alert(line)
```

---

## 5. Generator Expressions: The Memory-Saving Shortcut

Just like list comprehensions use `[]`, you can create a generator on the fly using parentheses `()`:

```python
# List comprehension (EAGER: computes all 1,000,000 squares in RAM immediately):
squares_list = [x ** 2 for x in range(1_000_000)]  # Takes ~8 Megabytes of RAM

# Generator expression (LAZY: computes squares one at a time on demand):
squares_gen = (x ** 2 for x in range(1_000_000))   # Takes only ~112 Bytes of RAM!

print("Next square:", next(squares_gen))  # 0
print("Next square:", next(squares_gen))  # 1
print("Next square:", next(squares_gen))  # 4
```

---

## 6. Quick Self-Test
1. What keyword transforms a regular Python function into a generator?
   - *Answer: `yield`.*
2. What happens to a generator's local variables when it hits a `yield` statement?
   - *Answer: They are frozen and preserved in the heap frame until `next()` is called again.*
