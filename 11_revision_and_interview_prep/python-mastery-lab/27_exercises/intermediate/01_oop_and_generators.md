# Intermediate Exercises: OOP, Generators & Protocols

## Exercise 1: The Lazy Chunking Generator
**Task**: Build a generator function `chunked(iterable, chunk_size: int)` that yields chunks of items of length `chunk_size` from any stream or large dataset without reading everything into memory at once.
```python
# Example:
# list(chunked(range(10), 3)) -> [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

---

## Exercise 2: Temperature Value with Descriptor Validation
**Task**: Create a descriptor `Temperature` that ensures a temperature value (in Celsius) cannot be set below absolute zero (`-273.15°C`). Raising `ValueError` if an invalid temperature is assigned.
```python
class WeatherStation:
    celsius = Temperature()

station = WeatherStation()
station.celsius = 25.0       # OK
station.celsius = -300.0     # Must raise ValueError!
```

---

## Exercise 3: Custom Context Manager for Database Transactions
**Task**: Write a context manager `transaction(connection)` using `@contextmanager` that automatically commits if the block executes cleanly, but rolls back if an exception occurs, re-raising the original exception.

---

## Exercise 4: Output Prediction Self-Check
What does this print?
```python
def make_multipliers():
    return [lambda x: i * x for i in range(4)]

multipliers = make_multipliers()
print([m(2) for m in multipliers])
```
<details>
<summary>Click to reveal answer</summary>

**Output**:
```
[6, 6, 6, 6]
```
**Why**: The infamous Late Binding Closure Trap! Lambdas do not capture the *value* of `i` when created; they capture the *name* `i`. By the time `m(2)` is called, the loop has completed and `i` equals `3` for all closures.  
**Fix**: `lambda x, i=i: i * x` (default argument evaluates at definition time).
</details>
