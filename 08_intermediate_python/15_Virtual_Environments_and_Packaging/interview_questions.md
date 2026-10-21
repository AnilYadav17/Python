# 15. Virtual Environments & Packaging — Interview & Viva Questions

---

### Q1: How does Python know it is running inside a virtual environment?
**Model Answer:**
- Upon startup, the Python binary inspects the directory containing the executable and its parent directory for a file named `pyvenv.cfg`.
- If `pyvenv.cfg` is found:
  1. Python sets `sys.prefix` to the root directory of the virtual environment.
  2. It sets `sys.base_prefix` to the directory of the global host Python interpreter.
  3. It configures `sys.path` to look for third-party packages inside the virtual environment's `lib/pythonX.Y/site-packages` directory instead of the system-wide site-packages.
- Code can detect whether it is running in a virtual environment by checking `sys.prefix != sys.base_prefix`.

---

### Q2: What actually happens when you run `source .venv/bin/activate`?
**Model Answer:**
- `activate` is a shell script that performs three simple environment variable modifications in the current shell session:
  1. It prepends `.venv/bin` to the front of the shell's `$PATH` variable, ensuring that commands like `python` or `pip` resolve to the virtual environment's binaries first.
  2. It defines a shell function `deactivate` to restore the original `$PATH`.
  3. It updates the terminal prompt string (`PS1`) to display `(.venv)`.
- **Key Note**: Running `activate` is not strictly required. Directly executing `.venv/bin/python script.py` achieves the exact same isolated execution and is the standard approach in Dockerfiles, cron jobs, and production services.

---

### Q3: Why shouldn't you commit a `.venv` directory to Git?
**Model Answer:**
- **Platform Incompatibility**: Virtual environments contain OS-specific compiled binaries and symlinks (e.g. Linux ELF binaries vs Windows `.exe` wrappers). A virtual environment created on macOS or Linux will not run on Windows.
- **Hardcoded Absolute Paths**: Scripts inside `.venv/bin` contain hardcoded absolute shebang paths (e.g. `#!/home/user/project/.venv/bin/python`). Moving the directory to a different folder or machine breaks all binaries.
- **Repository Bloat**: Virtual environments contain hundreds of megabytes of third-party libraries that can easily be reconstructed in seconds by running `pip install -r requirements.txt` or `poetry install`.

---

### Q4: What is PEP 668 (`EXTERNALLY-MANAGED`) and why do modern Linux distros block global `pip install`?
**Model Answer:**
- PEP 668 defines a mechanism for operating systems to mark their system Python installation as "externally managed" by placing an `EXTERNALLY-MANAGED` marker file in the system site-packages directory.
- In modern Linux distributions (Debian 12+, Ubuntu 23.04+, Fedora), running `pip install` globally is blocked with `error: externally-managed-environment`.
- **Reason**: OS package managers (like `apt` or `dnf`) rely on system Python for core OS services. Installing unmanaged packages via `pip` globally can overwrite or conflict with system-critical libraries, corrupting the operating system.
- **Solution**: Always create and activate a project-specific virtual environment before using `pip`.

---

### Q5: What is the difference between a Wheel (`.whl`) and a Source Distribution (`sdist`)?
**Model Answer:**
- **Source Distribution (`sdist`, `.tar.gz`)**: Contains uncompiled source code, raw C/C++ files, and build scripts. When installed, `pip` must invoke a build backend to compile extensions locally, requiring C compilers and development headers on the user's system.
- **Built Wheel (`.whl`)**: A pre-compiled binary ZIP distribution (PEP 427). It contains ready-to-use Python files and pre-compiled shared libraries (`.so`/`.pyd`).
- **Benefits of Wheels**:
  - Extremely fast installation (direct file extraction into `site-packages`).
  - Zero compilation requirement: end users do not need C/C++ compilers installed on their machines.

---

### Q6: What is `pyproject.toml` and why is it replacing `setup.py`?
**Model Answer:**
- `pyproject.toml` is the unified declarative packaging configuration standard introduced in PEP 517, 518, and 621.
- **Why it replaces `setup.py`**:
  1. **Security & Static Analysis**: `setup.py` contained executable Python code that ran arbitrarily during dependency resolution and package builds. `pyproject.toml` is purely declarative TOML data that can be parsed safely without executing arbitrary code.
  2. **Build Tool Independence**: The `[build-system]` table decouples the package from Setuptools, allowing developers to use modern build backends like Flit, Hatch, Poetry, or Maturin without breaking `pip`.
  3. **Standardized Metadata**: PEP 621 standardizes metadata keys (`[project]`), making tool configurations consistent across the entire Python ecosystem.

---

### Q7: Why is the `src/` layout preferred over a flat layout for Python project repositories?
**Model Answer:**
- In a **flat layout**, the package directory sits directly in the root of the project next to tests:
  ```text
  my_repo/
  ├── my_package/
  └── tests/
  ```
  When you run `pytest` from the root directory, Python automatically adds the current working directory to `sys.path`. This causes tests to import the **local unbuilt source files** instead of the package installed in the virtual environment.
- In a **`src/` layout**:
  ```text
  my_repo/
  ├── src/my_package/
  └── tests/
  ```
  Because `src/` is not automatically on `sys.path`, running `pytest` fails unless the package has been properly installed via `pip install -e .`. This guarantees that missing files in `pyproject.toml`, broken manifest declarations, or uncompiled C extensions are detected during testing before deployment.
