# Lesson 06: `*args` and `**kwargs` (Flexible Arguments)

## 1. What Are `*args` and `**kwargs` in Simple Words?
Sometimes you don't know ahead of time how many arguments a user will pass to your function:
- A `sum_all()` function should accept 2 numbers, 5 numbers, or 100 numbers!
- A logger should accept arbitrary options.

Python gives you two special packing operators:
1. **`*args`**: Packs any number of **positional arguments into a Tuple**.
2. **`**kwargs`**: Packs any number of **keyword arguments into a Dictionary**.

*(Note: The words `args` and `kwargs` are conventions. It is the single asterisk `*` and double asterisk `**` that do the magic!)*

---

## 2. Using `*args` (Packing into a Tuple)

```python
def calculate_sum(*numbers):
    print("Type of numbers:", type(numbers))  # <class 'tuple'>
    print("Received tuple: ", numbers)
    return sum(numbers)

print(calculate_sum(10, 20))            # 30
print(calculate_sum(1, 2, 3, 4, 5, 6))  # 21
```

---

## 3. Using `**kwargs` (Packing into a Dictionary)

```python
def print_user_profile(username, **details):
    print(f"User: {username}")
    print("Type of details:", type(details))  # <class 'dict'>
    for key, value in details.items():
        print(f"  {key}: {value}")

print_user_profile("anil", role="Senior Engineer", city="Bangalore", level=5)
```
**Output:**
```
User: anil
Type of details: <class 'dict'>
  role: Senior Engineer
  city: Bangalore
  level: 5
```

---

## 4. Unpacking in Reverse: Passing Collections to Functions

You can also use `*` and `**` when **calling** a function to unpack a list or dict into separate arguments:

```python
def make_box(width, height, color):
    print(f"Box: {width}x{height}, Color: {color}")

# Unpack a list with *:
dimensions = [100, 200, "Blue"]
make_box(*dimensions)  # Same as make_box(100, 200, "Blue")

# Unpack a dict with **:
config = {"width": 50, "height": 80, "color": "Red"}
make_box(**config)     # Same as make_box(width=50, height=80, color="Red")
```

---

## 5. Quick Self-Test
1. What type does `*args` produce inside the function body?
   - *Answer: A `tuple`.*
2. What type does `**kwargs` produce inside the function body?
   - *Answer: A `dict`.*
