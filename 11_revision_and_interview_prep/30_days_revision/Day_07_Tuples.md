# Day 7: Tuples

## Explanation
Tuples are similar to lists but they are **immutable** (cannot be changed after creation). They are faster and safer for fixed data.

## Key Concepts
- **Creating**: `my_tuple = (1, 2, 3)` or `my_tuple = 1, 2, 3`.
- **Single Element Tuple**: Needs a comma, e.g., `(5,)`.
- **Immutability**: You cannot append or reassign items (`my_tuple[0] = 5` throws an error).
- **Unpacking**: Assigning tuple values to multiple variables.

## Code Example
```python
coordinates = (10, 20, 30)
x, y, z = coordinates # Unpacking
print(f"X: {x}, Y: {y}, Z: {z}")
```

## Task
Create a tuple of your favorite movies. Try to modify an element (observe the error). Then, unpack the tuple into individual variables.