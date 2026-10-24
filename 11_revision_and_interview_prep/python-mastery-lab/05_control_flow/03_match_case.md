# Lesson 03: Structural Pattern Matching (`match / case`)

## 1. What Is `match / case` in Simple Words?
Introduced in **Python 3.10**, `match / case` looks like a `switch` statement from other languages, but it is **far more powerful**.

It doesn't just check values—it inspects the **shape, structure, and contents** of data and automatically unpacks variables!

---

## 2. Basic Example: Replacing Long `if/elif` Chains

```python
status_code = 404

match status_code:
    case 200:
        print("Success OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Page Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        # The underscore '_' is the default wildcard fallback!
        print("Unknown status code")
```

---

## 3. Structural Matching and Unpacking (The Superpower)

Look at how `match` can parse different incoming command formats:

```python
def handle_command(command: list):
    match command:
        case ["QUIT"]:
            print("Exiting game...")
            
        case ["GO", direction]:
            # Automatically unpacks the 2nd item into 'direction'!
            print(f"Walking towards {direction}")
            
        case ["TELEPORT", x, y]:
            # Automatically unpacks coordinates!
            print(f"Teleporting to coordinates ({x}, {y})")
            
        case ["ATTACK", target, damage] if damage > 100:
            # Pattern matching with an 'if' Guard condition!
            print(f"CRITICAL HIT on {target} for {damage} damage!")
            
        case ["ATTACK", target, damage]:
            print(f"Normal attack on {target} for {damage} damage")
            
        case _:
            print("Invalid command syntax")

handle_command(["GO", "North"])       # Walking towards North
handle_command(["ATTACK", "Boss", 250]) # CRITICAL HIT on Boss for 250 damage!
```

---

## 4. Quick Self-Test
1. What does the wildcard `case _:` mean in a `match` statement?
   - *Answer: It matches anything (acts as the default `else` fallback).*
2. What is a "guard" in pattern matching?
   - *Answer: An additional `if` condition attached to a `case` clause (e.g. `case [x, y] if x > 0:`).*
