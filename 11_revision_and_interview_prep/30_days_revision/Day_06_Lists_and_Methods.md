# Day 6: Lists and Methods

## Explanation
Lists are mutable, ordered collections of items. They can hold mixed data types.

## Key Concepts
- **Creating**: `my_list = [1, 2, 'three']`.
- **Accessing**: Zero-indexed, negative indexing supported.
- **Methods**: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, `.extend()`.
- **Slicing**: Extracting sub-lists.

## Code Example
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
popped = fruits.pop(1) # removes 'banana'
fruits.sort()
print(f"List: {fruits}, Popped: {popped}")
```

## Task
Create a list of 5 random numbers. Add a new number to the end, insert one at index 2, sort the list in descending order, and print it.