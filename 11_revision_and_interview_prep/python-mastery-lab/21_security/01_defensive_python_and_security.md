# Lesson 21.1: Defensive Python — Security Pitfalls & Hardening

## 1. What Is This in Simple Words?
Writing code that works is only half the job. Writing code that **cannot be hacked** when malicious actors feed it poisoned data is what makes you an expert engineer.  
In Python, dynamic flexibility can be a double-edged sword if you don't know the critical security traps.

---

## 2. The 4 Deadly Sins of Python Security

### Sin #1: The `eval()` & `exec()` Execution Trap
Never, ever use `eval()` on data received from users or network requests.
```python
# VULNERABLE:
# user_input = "__import__('os').system('rm -rf /')"
# eval(user_input) -> System destroyed!

# DEFENSIVE FIX: Use ast.literal_eval for safe strings/numbers/lists
import ast
safe_data = ast.literal_eval("[1, 2, {'key': 'value'}]")  # SAFE!
```

### Sin #2: The Poisoned `pickle` Vulnerability (CWE-502)
Python's `pickle` serialization format is Turing-complete. Unpickling data executes code!
```python
# DEFENSIVE FIX: NEVER unpickle data received from untrusted clients or cookies!
# Always use JSON, YAML (SafeLoader), or Protocol Buffers.
import json

safe_json_bytes = json.dumps({"user": "alice", "id": 42})
data = json.loads(safe_json_bytes)  # 100% immune to arbitrary code execution
```

### Sin #3: Path Traversal (Directory Escape)
If you let users download a filename:
```python
from pathlib import Path

# VULNERABLE: user_input = "../../../../etc/passwd"
# DEFENSIVE FIX:
BASE_DIR = Path("/var/app/uploads").resolve()

def get_safe_filepath(filename: str) -> Path:
    target_path = (BASE_DIR / filename).resolve()
    # Verify that target_path is STRICTLY a child of BASE_DIR:
    if not target_path.is_relative_to(BASE_DIR):
        raise PermissionError("Access denied: Path traversal detected!")
    return target_path
```

### Sin #4: SQL Injection
```python
# VULNERABLE:
# query = f"SELECT * FROM users WHERE username = '{user_input}'"

# DEFENSIVE FIX: Always use parameterized queries (?)
# cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
```

---

## 3. Mind-Blowing Facts! 💡

> **Fact 1: `pickle` Can Run Shell Commands During Deserialization!**  
> An attacker can define a class with a custom `__reduce__()` dunder method that instructs Python's unpickler to invoke `os.system('curl evil.com')`. The moment your server calls `pickle.loads(payload)`, the command executes with the server's full privileges!
>
> **Fact 2: Python's `secrets` Module for Cryptography!**  
> Never use `random.randint()` or `random.choice()` for passwords, reset tokens, or cryptographic keys! The `random` module uses the Mersenne Twister algorithm, which can be reverse-engineered after observing just 624 outputs. Always use the built-in `secrets` module (`secrets.token_hex(32)`), which draws true cryptographically secure entropy from your operating system kernel!

---

## 4. Self-Test
1. **Question**: Why is `secrets.token_urlsafe(16)` preferred over `random.choice()` for generating password reset tokens?
   - *Answer*: `secrets` uses cryptographically secure random sources from the OS kernel, whereas `random` uses Mersenne Twister which is completely predictable.
