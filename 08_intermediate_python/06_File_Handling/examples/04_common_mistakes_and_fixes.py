"""
04_common_mistakes_and_fixes.py
Demonstrates common file handling mistakes and their fixes:
1. readlines() memory blowout vs stream iteration
2. Hardcoded path separators vs pathlib.Path
3. Leaking file descriptors by omitting context managers
"""

import tempfile
from pathlib import Path

def mistake_1_memory_streaming(work_dir: Path):
    print("--- 1. Memory Efficiency: readlines() vs Stream Iteration ---")
    data_file = work_dir / "lines.txt"

    # Write 10,000 lines
    with open(data_file, "w", encoding="utf-8") as f:
        for i in range(10_000):
            f.write(f"Record #{i:05d}: metadata payload\n")

    # BAD: f.readlines() loads EVERY line into a Python list in memory at once!
    # with open(data_file, "r") as f:
    #     all_lines = f.readlines()

    # FIX: Iterate directly over the file object (constant O(1) buffer memory)
    matching_count = 0
    with open(data_file, "r", encoding="utf-8") as f:
        for line in f:  # Streams one line at a time
            if "00050" in line:
                matching_count += 1
    print(f"Streamed 10,000 lines, found {matching_count} target match without RAM spike.")


def mistake_2_cross_platform_paths():
    print("\n--- 2. Cross-Platform Paths: Hardcoded Strings vs pathlib ---")
    # BAD: "data\\logs\\today.log" fails on Linux/macOS; "data/logs/today.log" may fail on old Windows APIs

    # FIX: Use pathlib.Path with the / division operator
    log_path = Path("var") / "log" / "app" / "service.log"
    print(f"Pathlib resolved path for current OS: {log_path}")
    print(f"Parent directory: {log_path.parent}")
    print(f"File suffix: {log_path.suffix}")


def mistake_3_resource_leaks(work_dir: Path):
    print("\n--- 3. Resource Leaks: open() without 'with' ---")
    # BAD: f = open("file.txt"); f.read(); # forgot f.close() -> leaks OS file descriptor!

    # FIX: Always use the 'with' statement
    test_file = work_dir / "safe.txt"
    test_file.write_text("Safe content", encoding="utf-8")

    with open(test_file, "r", encoding="utf-8") as f:
        data = f.read()
    # At this point, f is guaranteed closed:
    print(f"File descriptor closed status: {f.closed}")


def main():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)
        mistake_1_memory_streaming(p)
        mistake_2_cross_platform_paths()
        mistake_3_resource_leaks(p)

if __name__ == "__main__":
    main()
