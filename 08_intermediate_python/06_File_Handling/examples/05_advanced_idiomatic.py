"""
05_advanced_idiomatic.py
Demonstrates production-grade file operations:
1. High-performance chunked binary file streaming (SHA-256 calculation)
2. Atomic file write pattern (temp file write + atomic os.replace)
"""

import hashlib
import os
import tempfile
from pathlib import Path

def calculate_sha256_chunked(file_path: Path, chunk_size: int = 65536) -> str:
    """
    Computes SHA-256 hash of a file of arbitrary size in constant O(1) memory.
    """
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read stream in 64KB binary chunks using two-argument iter()
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def atomic_write_text(target_path: Path, content: str, encoding: str = "utf-8"):
    """
    Writes content to target_path atomically:
    1. Writes to temporary file in the same directory.
    2. Uses os.replace() to atomically overwrite the destination.
    Prevents corrupted partial files if the process crashes mid-write.
    """
    target_path = Path(target_path)
    parent_dir = target_path.parent
    parent_dir.mkdir(parents=True, exist_ok=True)

    # Create temporary file in the same directory/filesystem so rename is atomic
    with tempfile.NamedTemporaryFile("w", dir=parent_dir, delete=False, encoding=encoding) as tmp:
        tmp.write(content)
        temp_name = tmp.name

    # os.replace is atomic on both POSIX and Windows (Python 3.3+)
    os.replace(temp_name, target_path)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        work_dir = Path(tmp)

        print("--- 1. Atomic File Writing ---")
        dest_file = work_dir / "config" / "settings.json"
        initial_payload = '{"version": 1, "status": "INITIAL"}'
        atomic_write_text(dest_file, initial_payload)
        print(f"Initial file written atomically: '{dest_file.read_text()}'")

        # Overwrite atomically
        updated_payload = '{"version": 2, "status": "UPDATED_ATOMICALLY"}'
        atomic_write_text(dest_file, updated_payload)
        print(f"Updated file after atomic replace: '{dest_file.read_text()}'")

        print("\n--- 2. Chunked Binary Streaming & Hashing ---")
        # Create a sample binary file
        sample_bin = work_dir / "large_asset.bin"
        sample_bin.write_bytes(b"A" * 500_000 + b"B" * 500_000)  # 1MB file

        sha256_hash = calculate_sha256_chunked(sample_bin)
        print(f"Calculated SHA-256 for 1MB file in chunks: {sha256_hash}")

if __name__ == "__main__":
    main()
