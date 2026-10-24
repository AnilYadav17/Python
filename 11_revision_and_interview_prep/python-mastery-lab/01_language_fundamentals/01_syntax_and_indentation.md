# Lesson 01: Syntax and Indentation

## 1. What Is This in Simple Words?
In most programming languages (like C, Java, or JavaScript), curly brackets `{}` are used to show where a block of code starts and ends. 

In Python, we don't use curly brackets for code blocks. Instead, Python uses **indentation** (the blank spaces at the start of a line). 

Indentation in Python is not just for making code look neat—**it is a strict grammar rule**. The indentation tells Python which lines belong inside an `if` condition, a loop, or a function.

---

## 2. Why Did Python Choose Indentation?
1. **Readable by default**: In other languages, developers can write messy, unindented code that still runs. In Python, readable code is enforced by the compiler.
2. **Less visual clutter**: You don't have to worry about missing or mismatched closing brackets `}`.
3. **Consistency**: Everyone's Python code looks clean and structured in the same way.

---

## 3. The Rules of Indentation
- **Rule 1: Use 4 spaces per indentation level.** This is the official community standard (PEP 8).
- **Rule 2: Never mix Tabs and Spaces.** Mixing tabs and spaces causes confusing bugs because a tab might look like 4 spaces in your editor, but Python sees it as 8 spaces. In Python 3, mixing tabs and spaces raises an `IndentationError: unindent does not match any outer indentation level`.
- **Rule 3: A colon `:` signals the start of an indented block.** Whenever you write `if`, `else`, `for`, `while`, `def`, or `class`, you end the line with a colon `:`. The next line **must** be indented.
- **Rule 4: Empty blocks require `pass`.** If you write an `if` statement or function but don't have any code for it yet, you cannot leave it completely blank. You must write `pass`.

---

## 4. Simple Examples

### Correct Example:
```python
age = 20

if age >= 18:
    # This block has 4 spaces of indentation
    print("You are an adult.")
    print("You are eligible to vote.")

# This line has 0 spaces, so it runs after the if block finishes
print("Program finished.")
```

### What Happens If You Make a Mistake?

#### Mistake 1: Missing Indentation
```python
age = 20
if age >= 18:
print("Adult")
```
**Python Output:**
```
IndentationError: expected an indented block after 'if' statement on line 2
```

#### Mistake 2: Unexpected Indentation
```python
print("Hello")
    print("World")  # Why is this pushed forward?
```
**Python Output:**
```
IndentationError: unexpected indent
```

---

## 5. How Python Understands Indentation Internally
When Python reads your file, its **tokenizer** converts your spaces into special hidden signals:
- When a line moves to the right (deeper), Python creates an **`INDENT`** token.
- When a line moves back to the left (shallower), Python creates a **`DEDENT`** token.

Think of `INDENT` as `{` and `DEDENT` as `}` in other languages!

---

## 6. Common Misconception
> **Misconception:** *"Can I use 2 spaces instead of 4 spaces?"*
> 
> **Fact:** Python allows 2 spaces, 3 spaces, or 8 spaces, as long as you are 100% consistent within that block. However, **the global Python standard is strictly 4 spaces**. You should always configure your code editor to insert 4 spaces whenever you press the Tab key.

---

## 7. Quick Self-Test
1. What character must come before an indented block?
   - *Answer: A colon (`:`).*
2. What error does Python raise if you leave an `if` statement with no code inside it?
   - *Answer: `IndentationError: expected an indented block` (use `pass` if you want it empty).*
