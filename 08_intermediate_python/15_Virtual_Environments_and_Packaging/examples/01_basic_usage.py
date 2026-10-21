"""
01_basic_usage.py
Demonstrates virtual environment mechanics:
- Programmatically creating a virtual environment via venv.EnvBuilder
- Inspecting pyvenv.cfg configuration keys
- Examining sys.prefix vs sys.base_prefix
"""

import sys
import venv
import tempfile
from pathlib import Path

def demonstrate_venv_inspection():
    print("--- 1. Current Python Runtime Environment ---")
    print(f"Python Executable: {sys.executable}")
    print(f"sys.prefix:        {sys.prefix}")
    print(f"sys.base_prefix:   {sys.base_prefix}")

    # If sys.prefix != sys.base_prefix, we are inside a virtual environment!
    is_venv = sys.prefix != sys.base_prefix
    print(f"Is running inside a virtual environment? {is_venv}")


def demonstrate_programmatic_venv_creation(target_dir: Path):
    print("\n--- 2. Programmatic Virtual Environment Creation ---")
    venv_path = target_dir / "sample_venv"

    # Use standard library venv.EnvBuilder
    builder = venv.EnvBuilder(with_pip=False)
    print(f"Creating isolated virtual environment at: {venv_path.name}")
    builder.create(venv_path)

    # Verify generated structure
    cfg_file = venv_path / "pyvenv.cfg"
    print(f"pyvenv.cfg exists: {cfg_file.exists()}")

    # Read and inspect pyvenv.cfg
    print("\nContents of pyvenv.cfg:")
    for line in cfg_file.read_text().splitlines():
        print(f"  {line}")


def main():
    demonstrate_venv_inspection()
    with tempfile.TemporaryDirectory() as tmp_dir:
        demonstrate_programmatic_venv_creation(Path(tmp_dir))

if __name__ == "__main__":
    main()
