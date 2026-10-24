# Lesson 20.1: Performance Tuning — Profiling with `cProfile`, `tracemalloc`, & `__slots__`

## 1. What Is This in Simple Words?
Legendary computer scientist Donald Knuth famously stated:  
> *"Premature optimization is the root of all evil."*

Never guess where your code is slow. You will almost always guess wrong.  
- **Profiling**: Measuring exact runtime seconds and memory consumption line-by-line using scientific tools.
- **`cProfile`**: Python's built-in C-level CPU profiler that records every function call count and cumulative time.
- **`tracemalloc`**: Built-in memory profiler tracking exact line numbers where RAM was allocated.
- **`__slots__`**: An OOP optimization that strips the dynamic `__dict__` from class instances to save up to 60% memory!

---

## 2. Pinpoint CPU Bottlenecks with `cProfile`

Run `cProfile` directly from the command line:
```bash
python -m cProfile -s cumtime my_script.py
```
Or programmatically inside your code:
```python
import cProfile
import pstats

def slow_task():
    # Simulating work
    return [i ** 2 for i in range(1_000_000)]

profiler = cProfile.Profile()
profiler.enable()

slow_task()

profiler.disable()
stats = pstats.Stats(profiler).sort_stats("cumtime")
stats.print_stats(5)  # Print the top 5 most expensive functions
```

---

## 3. Memory Optimization with `__slots__`

Normally, every Python object has an internal `__dict__` dictionary so you can add attributes on the fly (`obj.color = 'red'`). But dictionaries take significant memory!  
If you instantiate 1,000,000 objects (like rows in a database), `__slots__` tells Python to use a tiny fixed-size C array instead:

```python
import sys

# Standard class with __dict__ overhead:
class NormalPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Optimized class with __slots__:
class SlottedPoint:
    __slots__ = ("x", "y")
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

p1 = NormalPoint(1.0, 2.0)
p2 = SlottedPoint(1.0, 2.0)

# Compare instance sizes:
# p1 has an entire __dict__ dictionary (~100-150 bytes total)
# p2 only has its two raw attributes (~48 bytes total)
print(f"Normal Point has __dict__: {hasattr(p1, '__dict__')}")   # True
print(f"Slotted Point has __dict__: {hasattr(p2, '__dict__')}") # False
```

---

## 4. Mind-Blowing Facts! 💡

> **Fact 1: Dot Lookup Tax!**  
> Every time Python sees `math.sin(x)` inside a loop of 10,000,000 iterations, it performs two dictionary lookups on every single loop iteration: finding `math` in globals, and then finding `sin` in `math`!  
> By simply aliasing it to a local variable:  
> `sin = math.sin`  
> before the loop, your loop can run **20% to 30% faster** because local variables use `LOAD_FAST`!
>
> **Fact 2: String Concatenation Trap!**  
> Writing `s += char` inside a loop creates a completely new string object and copies all previous characters into new memory every iteration, leading to $O(N^2)$ quadratic slowdown! Always append strings to a `list` and use `"".join(chunks)` for $O(N)$ speed!

---

## 5. Self-Test
1. **Question**: When should you NOT use `__slots__`?
   - *Answer*: When you need dynamic runtime attributes added to instances, when multiple inheritance conflicts with slotted classes, or for simple small classes where memory is negligible.
