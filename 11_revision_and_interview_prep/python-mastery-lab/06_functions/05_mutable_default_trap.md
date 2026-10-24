# Lesson 05: The Mutable Default Argument Trap

## 1. The Most Famous Bug in Python

Look at this function written by a developer:
```python
def add_player(name, team=[]):
    team.append(name)
    return team
```
It looks completely harmless! If you don't supply a `team`, it defaults to an empty list `[]`.

Now, watch what happens when we call it:
```python
team_alpha = add_player("Alice")
print("Team Alpha:", team_alpha)
# Team Alpha: ['Alice']  (Looks good so far!)

team_beta = add_player("Bob")
print("Team Beta:", team_beta)
# Team Beta: ['Alice', 'Bob']  <-- WHAT?! Bob was added to Alice's team!

team_gamma = add_player("Charlie")
print("Team Gamma:", team_gamma)
# Team Gamma: ['Alice', 'Bob', 'Charlie']  <-- The list never resets!
```

---

## 2. Why Did This Happen? (Function Definition vs. Call Time)

In most other languages, default arguments are created fresh every time the function is called.

> **In Python, default arguments are evaluated ONLY ONCE, at the exact moment the function is DEFINED (when Python compiles the `def` line)!**

- When Python first reads `def add_player(name, team=[]):`, it creates **one single empty list** in RAM.
- Python attaches that list directly to the function object in an attribute called **`add_player.__defaults__`**.
- Every time you call `add_player()` without a second argument, Python passes that **same exact list from `__defaults__`**!
- Since lists are mutable, appending to it changes the shared list forever.

### Prove It to Yourself:
```python
print(add_player.__defaults__)
# Output: (['Alice', 'Bob', 'Charlie'],)
# The default list literally holds all previous values!
```

---

## 3. The Professional Fix: The `None` Sentinel Pattern

Whenever you want a default argument to be a mutable collection (a list, a dictionary, or a set), **always use `None` as the default**:

```python
# THE CORRECT, PRODUCTION-GRADE PATTERN:
def add_player(name, team=None):
    if team is None:
        team = []  # Creates a brand-new, isolated empty list every single call!
    team.append(name)
    return team
```

Now every call without an argument gets its own fresh, isolated list:
```python
print(add_player("Alice"))   # ['Alice']
print(add_player("Bob"))     # ['Bob']  (100% safe!)
```

---

## 4. Quick Self-Test
1. When are default parameter values evaluated in Python?
   - *Answer: Only once, at function definition time (when the `def` line is executed).*
2. Where are default argument values stored in memory?
   - *Answer: In the function object's `__defaults__` attribute.*
3. What is the standard idiom to safely use an empty list as a default argument?
   - *Answer: Set default to `None`, then initialize `team = []` inside the function body if `team is None`.*
