# Expert Exercises: Metaclasses, Descriptors & Bytecode Introspection

## Exercise 1: The Singleton Metaclass
**Task**: Implement a metaclass `SingletonMeta(type)` that ensures any class instantiated with `metaclass=SingletonMeta` only ever produces a single instance in memory across the entire program runtime.
```python
class DatabaseConnection(metaclass=SingletonMeta):
    pass

c1 = DatabaseConnection()
c2 = DatabaseConnection()
assert c1 is c2
```

---

## Exercise 2: Type-Enforcing Descriptor
**Task**: Build a generic descriptor `Typed(expected_type)` that enforces runtime type validation inside `__set__`:
```python
class Person:
    name = Typed(str)
    age = Typed(int)

p = Person()
p.name = "Alice"  # OK
p.age = "twenty"  # Raises TypeError: Expected int, got str
```

---

## Exercise 3: Bytecode Instruction Counter
**Task**: Using Python's `dis.get_instructions()`, write a function `analyze_bytecode_complexity(func)` that counts how many total bytecode opcodes are executed and returns a dictionary tallying the frequency of each opcode (e.g. how many `LOAD_FAST` vs `LOAD_GLOBAL` calls).

---

## Exercise 4: Deep Python Quiz
Why does modifying `sys.modules` allow you to implement hot-reloading or mock entire libraries at runtime?  
<details>
<summary>Click to reveal answer</summary>

**Answer**: When an `import` statement executes, Python's first step is to check if the module key exists in the `sys.modules` dictionary. If present, Python immediately returns that cached object without touching the filesystem. By modifying or mutating `sys.modules["target_module"]`, you directly alter what subsequent `import` statements receive throughout the entire process!
</details>
