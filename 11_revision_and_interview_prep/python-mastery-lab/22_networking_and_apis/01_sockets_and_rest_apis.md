# Lesson 22.1: Networking & APIs — From Raw Sockets to REST Endpoints

## 1. What Is This in Simple Words?
Networking is how computers talk to each other across the room or across the globe:
- **Sockets**: The absolute lowest-level pipe for data. Think of it like plugging in a raw phone cable between two machines.
- **HTTP**: The high-level language of the Web built on top of TCP sockets. Clients send requests (`GET`, `POST`), servers return responses with status codes (`200 OK`, `404 Not Found`).
- **REST APIs**: Structured JSON data exchanges between applications.

---

## 2. Low-Level TCP Socket in Pure Python

Here is a minimal TCP Echo Server using only Python's built-in `socket` module:

```python
import socket

def run_simple_server():
    # AF_INET = IPv4, SOCK_STREAM = TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable address reuse so restarting server doesn't fail with "Address already in use":
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind(("127.0.0.1", 9999))
    server.listen(1)
    print("Server listening on 127.0.0.1:9999...")

    try:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        if data:
            conn.sendall(b"ECHO: " + data)
        conn.close()
    finally:
        server.close()
```

---

## 3. Clean HTTP Requests with `urllib.request`

You don't even need third-party packages to make authenticated HTTP GET/POST calls with JSON:

```python
import urllib.request
import json

def fetch_json_data(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "PythonMasteryLab/1.0", "Accept": "application/json"}
    )
    
    # Always set a timeout! Default socket timeout is infinite, which can hang forever!
    with urllib.request.urlopen(req, timeout=5) as response:
        if response.status == 200:
            raw_bytes = response.read()
            return json.loads(raw_bytes.decode("utf-8"))
        raise RuntimeError(f"HTTP Error: {response.status}")
```

---

## 4. Mind-Blowing Facts! 💡

> **Fact 1: The Infinite Hang Trap!**  
> In Python's `urllib.request` (and even in older versions of `requests`), if you omit the `timeout=` parameter, Python waits on the socket **forever**! If a remote server accepts the connection but never sends bytes, your entire server thread or process hangs indefinitely, exhausting all worker slots in production!
>
> **Fact 2: Little Endian vs Big Endian in Network Bytes!**  
> Computers store multi-byte numbers in memory in different byte orders (x86 CPU is Little Endian). But the Internet requires **Network Byte Order (Big Endian)**! Python's built-in `struct` module handles this conversion with the `!` character:
> ```python
> import struct
> # Convert integer 1024 to 2 network bytes:
> network_bytes = struct.pack("!H", 1024)
> print(list(network_bytes))  # [4, 0]
> ```

---

## 5. Self-Test
1. **Question**: Why is `timeout=` mandatory in production HTTP network calls?
   - *Answer*: Without a timeout, a slow or unresponsive server can hang your Python process indefinitely, starving system resources.
