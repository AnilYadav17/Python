# Lesson 08: Bytes (`bytes`) and Bytearray (`bytearray`)

## 1. Text vs. Raw Binary Data

- **`str` (Text)**: Human-readable Unicode text ("Hello", "नमस्ते").
- **`bytes` (Binary)**: The raw 8-bit numbers (`0` to `255`) that physical network cables and hard drives actually store.

```
       Human Text (str)
             │
             │ .encode('utf-8')   (Turns text into binary bytes)
             ▼
       Raw Bytes (bytes)
             │
             │ .decode('utf-8')   (Turns binary bytes back into text)
             ▼
       Human Text (str)
```

---

## 2. Creating and Inspecting `bytes`

You create a bytes literal by putting a **`b`** in front of quotes:
```python
raw_data = b"Hello"
print(type(raw_data))  # <class 'bytes'>
print(raw_data)        # b'Hello'
```

### Notice:
When you index a string, you get a 1-character string:
```python
print("Hello"[0])  # 'H' (str)
```
When you index a `bytes` object, you get the **raw integer ASCII byte value (0-255)**:
```python
print(b"Hello"[0])  # 72 (ASCII code for 'H'!)
```

---

## 3. `bytes` (Immutable) vs. `bytearray` (Mutable)

Just like `tuple` vs `list`:
- **`bytes`** is **immutable** (cannot be altered after creation).
- **`bytearray`** is **mutable** (you can modify individual bytes in-place!).

```python
# bytes is unchangeable:
b = b"Cat"
# b[0] = 66  # TypeError: 'bytes' object does not support item assignment

# bytearray can be changed in-place!
ba = bytearray(b"Cat")
ba[0] = 66  # 66 is ASCII for 'B'
print(ba)   # bytearray(b'Bat')
```

---

## 4. Where Do You Use Bytes?
1. **Reading Binary Files**: Images (`.png`, `.jpg`), audio (`.mp3`), PDFs.
2. **Network Programming**: Sending packets over TCP/UDP sockets.
3. **Cryptography & Hashing**: Password hashing with `hashlib` requires bytes input.

---

## 5. Quick Self-Test
1. What does `"Python".encode("utf-8")` return?
   - *Answer: A `bytes` object: `b'Python'`.*
2. Can you modify a byte inside a `bytearray`?
   - *Answer: Yes, `bytearray` is the mutable counterpart of `bytes`.*
