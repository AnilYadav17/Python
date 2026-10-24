# Lesson 02: Tokens and Lexing

## 1. What Is This in Simple Words?
When you read a sentence in English:
`"Python is easy to learn."`
Your brain doesn't see random letters. Your brain groups letters into **words** and **punctuation**.

Python does the exact same thing! When Python reads your code:
`total = 10 + 20`
It does not look at individual characters one by one. It groups them into meaningful chunks called **tokens**. 

The program inside Python that does this splitting is called the **Lexer** (or Tokenizer).

---

## 2. The 6 Types of Tokens in Python

Every single piece of Python code is made up of just six types of tokens:

1. **Keywords**: Reserved words with special meanings (e.g., `if`, `for`, `while`, `def`, `class`).
2. **Identifiers (Names)**: Names you create for variables, functions, and classes (e.g., `score`, `calculate_total`).
3. **Literals (Raw Values)**: Fixed values written directly in code (e.g., `42`, `3.14`, `"Hello"`, `True`).
4. **Operators**: Symbols that do calculations or comparisons (e.g., `+`, `-`, `*`, `==`, `<`).
5. **Delimiters (Punctuation)**: Symbols that separate things (e.g., `,`, `:`, `(`, `)`, `[`, `]`, `{}`).
6. **Layout Tokens**: Invisible markers Python creates for line breaks and indentation (`NEWLINE`, `INDENT`, `DEDENT`).

---

## 3. Step-by-Step Example

Let's look at this line of code:
```python
score = 95
```

Here is how the Python Lexer chops this line into tokens:

| Token Number | Token Category | Token Text | What It Means to Python |
| :--- | :--- | :--- | :--- |
| 1 | `NAME` | `'score'` | A variable name chosen by the programmer. |
| 2 | `OP` | `'='` | The assignment operator (store a value). |
| 3 | `NUMBER` | `'95'` | An integer number literal. |
| 4 | `NEWLINE` | `'\n'` | End of this instruction. |

---

## 4. Why Do We Care About Tokens?
1. **Syntax Errors happen during tokenizing**: If you write an invalid character (like a stray backtick or bad quote), the lexer fails immediately before even trying to run your code.
2. **Understanding keywords**: The lexer knows that `while` is a special command, not a variable name.

---

## 5. Try It Yourself in Python
You can use Python's built-in `tokenize` tool to see how Python breaks down any line of code:

```python
import io
import tokenize

code = "x = 10 + 5"
# Convert the string to bytes and feed it to the tokenizer
tokens = tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline)

for tok in tokens:
    if tok.string.strip():  # ignore empty spacing
        print(f"Token: {tok.string:<10} Type: {tokenize.tok_name[tok.type]}")
```

**Output:**
```
Token: x          Type: NAME
Token: =          Type: OP
Token: 10         Type: NUMBER
Token: +          Type: OP
Token: 5          Type: NUMBER
```

---

## 6. Key Takeaway
Before Python runs or calculates anything, it always turns your text into a clean list of **Tokens**. If the tokens don't follow Python's grammar, you get a `SyntaxError` immediately.
