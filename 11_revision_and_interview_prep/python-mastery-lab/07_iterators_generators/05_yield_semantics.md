# Lesson 05: `yield from` and Two-Way Generators

## 1. What Is `yield from` in Simple Words?
Imagine you have multiple small lists or generators, and you want to yield all their items in order:

```python
# The Clunky Old Way:
def chain_old():
    for x in [1, 2, 3]:
        yield x
    for y in ["a", "b", "c"]:
        yield y

# The Modern 'yield from' Way (PEP 380):
def chain_modern():
    yield from [1, 2, 3]          # Directly delegates to the first iterable!
    yield from ["a", "b", "c"]    # Directly delegates to the second iterable!

print(list(chain_modern()))
# Output: [1, 2, 3, 'a', 'b', 'c']
```

`yield from <iterable>` is a transparent pipeline that delegates control to a sub-iterator.

---

## 2. Fascinating Fact 💡
> **Did you know?**
> Before Python had the modern `async` and `await` keywords (added in Python 3.5), all asynchronous programming in Python was done using `@asyncio.coroutine` and `yield from`!  
> A Python coroutine is literally an evolved generator where `yield from` handed control back and forth to the event loop!

---

## 3. Two-Way Communication: Sending Data INTO a Generator (`.send()`)

Most people think generators only send data OUT to the caller.  
Generators can also receive data IN from the caller using **`.send()`**!

```python
def running_average():
    total = 0.0
    count = 0
    average = None

    while True:
        # yield 'average' to caller AND receive 'val' sent back in!
        val = yield average
        if val is None:
            break
        total += val
        count += 1
        average = total / count

# Start the generator:
avg_calc = running_average()
next(avg_calc)  # "Prime" the generator up to the first yield!

print(avg_calc.send(10))  # 10.0
print(avg_calc.send(20))  # 15.0 (Average of 10 and 20)
print(avg_calc.send(30))  # 20.0 (Average of 10, 20, 30)
```

---

## 4. Quick Self-Test
1. What does `yield from [1, 2, 3]` do?
   - *Answer: It iterates over `[1, 2, 3]` and yields each element one by one to the caller.*
2. How do you send a value into a paused generator?
   - *Answer: By calling `generator.send(value)`.*
