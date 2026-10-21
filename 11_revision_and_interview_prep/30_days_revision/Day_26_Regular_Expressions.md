# Day 26: Regular Expressions (Regex)

## Explanation
Regular expressions are powerful patterns used to search, extract, and manipulate strings.

## Key Concepts
- **`re` module**: Python's built-in regex library.
- **Methods**: `re.search()`, `re.match()`, `re.findall()`, `re.sub()`.
- **Meta-characters**: `\d` (digit), `\w` (word character), `+` (1 or more), `*` (0 or more), `^` (start), `$` (end).

## Code Example
```python
import re
text = "Contact me at info@example.com today!"
pattern = r'[\w.-]+@[\w.-]+'
match = re.search(pattern, text)
if match:
    print("Found email:", match.group())
```

## Task
Write a regex to extract all phone numbers in the format `XXX-XXX-XXXX` from a given string.