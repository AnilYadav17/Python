"""
02_edge_cases.py
Demonstrates virtual environment edge cases:
- include-system-site-packages flag impact
- Direct binary invocation vs shell activation script
- Relocation breakage (why moving a venv breaks it)
"""

import sys
import tempfile
from pathlib import Path

def demonstrate_activation_vs_direct_call():
    print("--- 1. Direct Binary Invocation vs Shell Activation ---")
    print("Key Insight: You do NOT need 'source .venv/bin/activate' to run Python in a venv!")
    print("Executing '/path/to/.venv/bin/python script.py' directly sets sys.prefix automatically.")
    print("Activation only modifies the shell's $PATH variable for convenience.")


def demonstrate_venv_relocation_trap():
    print("\n--- 2. Virtual Environment Relocation Trap ---")
    # Virtual environments contain hardcoded absolute paths inside:
    # 1. bin/activate scripts
    # 2. shebang lines of entry-point scripts (e.g. #!/home/user/project/.venv/bin/python)
    # 3. pyvenv.cfg home directory
    # Moving or renaming a .venv folder breaks these hardcoded paths!
    print("Tip: Never move or copy a .venv directory across folders or machines. Delete and recreate it.")


def main():
    demonstrate_activation_vs_direct_call()
    demonstrate_venv_relocation_trap()

if __name__ == "__main__":
    main()
