# Lesson 08: The Loop `else` Clause (A Unique Python Feature)

## 1. What Is Loop `else` in Simple Words?
In Python, both `for` loops and `while` loops can have an **`else:`** block attached to the end!

```python
for item in items:
    # do something
else:
    # when does this run?!
```

Most beginners assume: *"Oh, `else` runs if the loop condition was false."*  
**That is NOT how loop `else` works!**

> **The True Rule: The `else` block runs ONLY IF the loop finishes completely WITHOUT encountering a `break`!**

Think of loop `else` as: **"No Break Occurred"**.

---

## 2. A Crystal-Clear Example: The Prime Number Finder

Let's test if a number is prime (divisible only by 1 and itself):

```python
target = 13

for divisor in range(2, target):
    if target % divisor == 0:
        print(f"{target} is not prime (divisible by {divisor})")
        break  # We hit break! The loop terminates early!
else:
    # This ONLY runs if the loop checked ALL numbers and NEVER hit break!
    print(f"{target} is a PRIME number!")
```

### Notice:
In other languages, you have to create a clumsy flag variable:
`found = False ... if not found: ...`.  
In Python, the loop `else` makes flag variables completely unnecessary!

---

## 3. Quick Self-Test
1. If a loop executes a `break` statement, will the loop's `else` block execute?
   - *Answer: NO. The `else` block is skipped whenever a `break` occurs.*
2. If a loop is given an empty list `for x in []:`, will the `else` block run?
   - *Answer: YES! The loop ran 0 times, but it never hit a `break`, so `else` executes immediately.*
