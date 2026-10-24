# Lesson 09: Operator Precedence Quick Reference

## 1. Operator Priority Hierarchy

When expressions have multiple operators, Python computes them in this order:

1. **`()` Parentheses**: Always computed first.
2. **`x[i]`, `x.attr`, `f()`**: Indexing, attribute access, function calls.
3. **`**` Exponentiation**: Power (Right-to-Left: `2 ** 3 ** 2 = 512`).
4. **`+x`, `-x`, `~x`**: Unary signs and bitwise NOT.
5. **`*`, `/`, `//`, `%`**: Multiplicative math.
6. **`+`, `-`**: Additive math.
7. **`<<`, `>>`**: Bit shifts.
8. **`&`**: Bitwise AND.
9. **`^`**: Bitwise XOR.
10. **`\|`**: Bitwise OR.
11. **`==`, `!=`, `<`, `<=`, `>`, `>=`, `in`, `is`**: Comparisons.
12. **`not`**: Boolean negation.
13. **`and`**: Logical AND.
14. **`or`**: Logical OR.
15. **`:=`**: Walrus assignment.

---

## 2. Best Practice Reminder
Whenever your calculation mixes different categories of operators (e.g. arithmetic + comparison + boolean), **always wrap each logical piece in parentheses `()`**:

```python
# Unclear:
if x + 5 > 10 and not y or z == 2:

# Clean & Professional:
if ((x + 5) > 10 and (not y)) or (z == 2):
```
