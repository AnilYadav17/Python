"""
01_basic_usage.py
Demonstrates core file handling operations:
- Reading and writing text files with encoding="utf-8"
- Binary file operations (bytes)
- Context management with 'with'
- File pointer navigation (seek and tell)
"""

import tempfile
from pathlib import Path

def demonstrate_text_file_io(work_dir: Path):
    print("--- 1. Text File I/O ---")
    text_file = work_dir / "sample.txt"

    # Writing text with explicit UTF-8 encoding
    with open(text_file, "w", encoding="utf-8") as f:
        f.write("Line 1: Hello Python!\n")
        f.write("Line 2: Unicode support: 🐍 🚀\n")
        f.write("Line 3: File handling made simple.\n")

    # Reading line-by-line using iterator (memory efficient)
    print(f"Reading from {text_file.name}:")
    with open(text_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            print(f"  [{line_num}] {line.strip()}")


def demonstrate_binary_io(work_dir: Path):
    print("\n--- 2. Binary File I/O ---")
    binary_file = work_dir / "binary.dat"

    # Writing raw bytes
    raw_payload = bytes([0xDE, 0xAD, 0xBE, 0xEF, 0x00, 0xFF])
    with open(binary_file, "wb") as f:
        f.write(raw_payload)

    # Reading raw bytes
    with open(binary_file, "rb") as f:
        read_bytes = f.read()
    print(f"Written {len(raw_payload)} bytes, read: {read_bytes.hex().upper()}")


def demonstrate_seek_and_tell(work_dir: Path):
    print("\n--- 3. File Pointer: seek() and tell() ---")
    stream_file = work_dir / "seek_demo.txt"

    with open(stream_file, "w+", encoding="utf-8") as f:
        f.write("ABCDEFGHIJ")
        print(f"Pointer position after writing 10 characters: {f.tell()}")

        # Move pointer back to position 3 (0-indexed: 4th character)
        f.seek(3)
        print(f"Pointer position after seek(3): {f.tell()}")
        remaining = f.read()
        print(f"Read from position 3 to end: '{remaining}'")

        # Reset pointer back to beginning
        f.seek(0)
        print(f"Read entire content after seek(0): '{f.read()}'")


def main():
    # Use temporary directory for clean, isolated tests
    with tempfile.TemporaryDirectory() as tmp_dir:
        dir_path = Path(tmp_dir)
        demonstrate_text_file_io(dir_path)
        demonstrate_binary_io(dir_path)
        demonstrate_seek_and_tell(dir_path)

if __name__ == "__main__":
    main()
