# Practical Exercises: Fundamentals & Control Flow

## Exercise 1: FizzBuzz with Modern Pattern Matching
**Task**: Implement the classic FizzBuzz from 1 to 50, but instead of multiple `if/elif` statements, use Python 3.10 `match (i % 3 == 0, i % 5 == 0):`.
```python
# Expected output:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz...
```

---

## Exercise 2: Safe User Input Parser
**Task**: Write a function `parse_integer_list(raw_input: str) -> list[int]` that takes a comma-separated string (e.g. `"10, 25, abc, 40, -5"`) and returns only valid integers `[10, 25, 40, -5]`, gracefully skipping malformed entries using `try...except ValueError`.

---

## Exercise 3: Palindrome Checker with Two Pointers
**Task**: Check if a string is a palindrome (e.g. `"racecar"`, `"A man a plan a canal Panama"`), ignoring spaces and casing, without creating a reversed copy of the string (`[::-1]`). Use two pointers (`left` and `right`) for $O(1)$ memory efficiency!

---

## Exercise 4: Output Prediction Self-Check
What does this print and why?
```python
x = [1, 2, 3]
y = x
x += [4]
print(x)
print(y)
print(x is y)
```
<details>
<summary>Click to reveal answer</summary>

**Output**:
```
[1, 2, 3, 4]
[1, 2, 3, 4]
True
```
**Why**: For lists, `+=` calls `__iadd__()` which mutates the existing list in-place rather than allocating a new object. Because `y` references the exact same list in memory, both reflect the change!
</details>
