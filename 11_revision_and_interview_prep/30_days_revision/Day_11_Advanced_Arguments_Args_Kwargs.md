# Day 11: Advanced Arguments (*args and **kwargs)

## Explanation
Sometimes you don't know how many arguments will be passed to your function. Python provides `*args` and `**kwargs` to handle variable-length arguments.

## Key Concepts
- **`*args`**: Collects positional arguments into a tuple.
- **`**kwargs`**: Collects keyword arguments into a dictionary.
- **Order of parameters**: Standard args, `*args`, Default args, `**kwargs`.

## Code Example
```python
def order_pizza(size, *toppings, **details):
    print(f"Size: {size}")
    print(f"Toppings: {toppings}")
    print(f"Details: {details}")

order_pizza('Large', 'Pepperoni', 'Olives', delivery=True, tip=5)
```

## Task
Write a function that accepts any number of integers using `*args` and returns their product. Then call it with 4 different numbers.