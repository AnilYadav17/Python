# Lesson 14: Decorators (`@`) and `functools.wraps`

## 1. What Is a Decorator in Simple Words?
Imagine you have a plain coffee. A decorator is like adding whipped cream and chocolate sprinkles on top:
- It **decorates** the coffee.
- It doesn't change the coffee inside, but it adds extra goodness!

In Python, a **Decorator** is a function that takes another function, wraps extra functionality around it (like logging, timing, authentication, or caching), and returns the enhanced function.

---

## 2. The `@` Syntactic Sugar

Whenever you see:
```python
@timer
def process_data():
    pass
```
This is simply a clean shortcut for:
```python
process_data = timer(process_data)
```

---

## 3. Building Your First Decorator from Scratch (An Execution Timer)

```python
import functools
import time

def timer(func):
    # functools.wraps preserves the original function's name and docstring!
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        # Call the original function:
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        print(f"[TIMING] {func.__name__}() took {end_time - start_time:.6f} seconds")
        
        return result
    
    return wrapper
```

### Let's Use It:
```python
@timer
def heavy_calculation(n):
    """Calculates sum of squares."""
    return sum(i * i for i in range(n))

output = heavy_calculation(1_000_000)
print("Output:", output)
```

**Output:**
```
[TIMING] heavy_calculation() took 0.048123 seconds
Output: 333332833333500000
```

---

## 4. Why `@functools.wraps` Is Non-Negotiable!

If you forget `@functools.wraps(func)`:
```python
print(heavy_calculation.__name__)  # Prints 'wrapper' instead of 'heavy_calculation'!
print(heavy_calculation.__doc__)   # Prints None! The docstring was wiped out!
```
`@functools.wraps` copies over the function's real name, docstring, and metadata so debugging tools and `help()` work properly.

---

## 5. Quick Self-Test
1. What does `@my_decorator` do behind the scenes to `def func():`?
   - *Answer: It executes `func = my_decorator(func)`.*
2. Why should you always use `@functools.wraps(func)` inside your decorator?
   - *Answer: To preserve the original function's `__name__`, `__doc__`, and metadata.*
