"""
04_common_mistakes_and_fixes.py
Demonstrates common context manager traps and fixes:
1. Missing try-finally in @contextmanager (cleanup bypassed on exception)
2. Managing dynamic variable number of resources using contextlib.ExitStack
"""

import tempfile
from pathlib import Path
from contextlib import contextmanager, ExitStack

def mistake_1_missing_try_finally_in_generator():
    print("--- 1. Missing try-finally in @contextmanager Trap ---")

    # BUGGY: If an exception occurs in the with block, code after yield NEVER runs!
    cleanup_ran_buggy = False
    @contextmanager
    def buggy_manager():
        nonlocal cleanup_ran_buggy
        print("  [Buggy] Starting...")
        yield "resource"
        cleanup_ran_buggy = True  # BYPASSED on exception!

    try:
        with buggy_manager():
            raise RuntimeError("Boom!")
    except RuntimeError:
        pass
    print(f"  Did buggy cleanup run? {cleanup_ran_buggy} (LEAKED!)")

    # FIXED: Always enclose yield inside try-finally!
    cleanup_ran_fixed = False
    @contextmanager
    def fixed_manager():
        nonlocal cleanup_ran_fixed
        print("  [Fixed] Starting...")
        try:
            yield "resource"
        finally:
            cleanup_ran_fixed = True  # GUARANTEED to run!

    try:
        with fixed_manager():
            raise RuntimeError("Boom!")
    except RuntimeError:
        pass
    print(f"  Did fixed cleanup run? {cleanup_ran_fixed} (PROTECTED!)")


def mistake_2_dynamic_resource_management():
    print("\n--- 2. Dynamic Resources with ExitStack ---")
    # Opening 3 files dynamically without ExitStack requires clumsy nesting:
    # with open(f1) as a:
    #   with open(f2) as b:
    #     with open(f3) as c: ...
    # But what if the number of files is determined at runtime (e.g. 10 files)?

    # FIX: Use contextlib.ExitStack
    with tempfile.TemporaryDirectory() as tmp_dir:
        base = Path(tmp_dir)
        file_paths = [base / f"file_{i}.txt" for i in range(3)]
        for p in file_paths:
            p.write_text(f"Payload from {p.name}")

        print("Opening dynamic list of files cleanly with ExitStack:")
        with ExitStack() as stack:
            # Dynamically enter as many files as needed
            file_handles = [stack.enter_context(open(p, "r", encoding="utf-8")) for p in file_paths]
            for fh in file_handles:
                print(f"  Read: '{fh.read()}'")
        # All file handles are guaranteed closed when ExitStack exits
        print(f"All files closed: {all(fh.closed for fh in file_handles)}")


def main():
    mistake_1_missing_try_finally_in_generator()
    mistake_2_dynamic_resource_management()

if __name__ == "__main__":
    main()
