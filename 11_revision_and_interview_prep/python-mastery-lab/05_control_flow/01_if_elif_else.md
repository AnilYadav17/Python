# Lesson 01: Conditional Branching (`if`, `elif`, `else`)

## 1. What Is Conditional Branching?
Programs make decisions based on conditions:

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Needs Improvement")
```

---

## 2. The Conditional Expression (Ternary Operator)

In C or JavaScript, you write `condition ? a : b`.  
In Python, we write it in plain English:

```python
# Syntax: value_if_true if condition else value_if_false
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"
```

---

## 3. Quick Self-Test
1. In an `if / elif / else` block, if the `if` condition is True, will Python check the `elif` conditions below it?
   - *Answer: No, Python skips all subsequent `elif` and `else` branches as soon as one branch evaluates to True.*
