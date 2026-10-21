# 15. Virtual Environments & Packaging: Complete Reference

---

## 1. Why Isolated Environments Matter

### What it is
- A **virtual environment** is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.
- **Dependency Hell**: When Project A requires `urllib3==1.26.0` and Project B requires `urllib3==2.1.0`. In a global environment, one project will inevitably break.
- **PEP 668 (`EXTERNALLY-MANAGED`)**: Modern Linux distributions (Debian, Ubuntu, Fedora) mark system Python as externally managed, intentionally blocking global `pip install` to prevent breaking OS tools (like `apt` or `dnf`).

### Why it matters
- Prevents version collisions between different projects on the same development workstation.
- Guarantees project reproducibility across team members, CI/CD pipelines, and cloud containers.
- Protects the host operating system's system-level Python libraries from corruption.

### How it works (internals, if relevant)
- When Python boots up, it looks for a file named `pyvenv.cfg` in the directory above the executable.
- If `pyvenv.cfg` is present, Python initializes `sys.prefix` to the virtual environment path while pointing `sys.base_prefix` to the global host Python installation.
- Python appends the virtual environment's `site-packages` directory to `sys.path` and suppresses the global `site-packages`.

### Common mistakes / gotchas
- Running `sudo pip install <pkg>`: alters system files with root permissions, risking serious OS package corruption.
- Failing to use an isolated environment on modern Linux, triggering `error: externally-managed-environment`.

### Connects to
- The `venv` Module Architecture (subtopic 2 below).

---

## 2. The `venv` Module Architecture

### What it is
- The standard library module for creating lightweight virtual environments:
  ```bash
  python3 -m venv .venv
  ```
- Structure of a virtual environment:
  ```text
  .venv/
  ├── bin/ (or Scripts/ on Windows)
  │   ├── python -> symlink to host python3
  │   ├── pip
  │   └── activate
  ├── include/
  ├── lib/
  │   └── python3.X/
  │       └── site-packages/   # Installed 3rd-party packages
  └── pyvenv.cfg               # Core configuration metadata
  ```

### Why it matters
- Standardized, zero-dependency environment creator built directly into Python.
- Lightweight: stores symlinks to the base Python executable rather than copying entire multi-hundred-megabyte interpreter binaries.

### How it works (internals, if relevant)
- `pyvenv.cfg` contains three core keys:
  - `home`: Path to the directory containing the base Python executable.
  - `include-system-site-packages`: Boolean flag (`true` or `false`) determining whether packages from the base Python environment are visible.
  - `version`: Exact version of Python that created the environment.

### Common mistakes / gotchas
- Moving or renaming the `.venv` directory: virtual environment paths are hardcoded in wrapper scripts and symlinks. If moved, binaries fail. Solution: delete and recreate `.venv`.
- Checking `.venv/` into Git version control: virtual environments are platform-specific and must always be added to `.gitignore`.

### Connects to
- Activation and Deactivation (subtopic 3 below).

---

## 3. Activation and Deactivation

### What it is
- **Activation**:
  - POSIX: `source .venv/bin/activate`
  - Windows PowerShell: `.venv\Scripts\Activate.ps1`
- **Deactivation**: Run `deactivate` in the terminal session.

### Why it matters
- Activation is a shell convenience: it prepends `.venv/bin` to your shell's `$PATH` environment variable so typing `python` or `pip` automatically invokes the virtual environment's binaries.

### How it works (internals, if relevant)
- **Direct Invocation without Activation**:
  You do **NOT** have to run `source activate` to use a virtual environment!
  Executing `/path/to/.venv/bin/python script.py` or `/path/to/.venv/bin/pip install` automatically runs inside the virtual environment because the binary detects `pyvenv.cfg` in its parent directory.
- This direct invocation technique is standard practice in production Dockerfiles, cron jobs, systemd services, and CI/CD pipelines.

### Common mistakes / gotchas
- Trying to activate a virtual environment inside a child shell script with `source activate` and expecting the parent terminal session to remain activated (environment variable changes in child subshells do not propagate back to parent shells).
- In cron jobs, running `python script.py` assuming the virtual environment is active, which causes the cron job to invoke the wrong system Python. Always use `/path/to/.venv/bin/python`.

### Connects to
- Dependency Tracking with `requirements.txt` (subtopic 4 below).

---

## 4. Dependency Tracking & `requirements.txt`

### What it is
- Standard plain-text file listing project dependencies and version specifiers (PEP 508):
  - `requests==2.31.0` (exact pin)
  - `fastapi>=0.100.0,<0.105.0` (range)
  - `flask~=3.0.0` (compatible release: $\ge 3.0.0, < 3.1.0$)
- Commands:
  - `pip freeze > requirements.txt`: Dumps all currently installed packages.
  - `pip install -r requirements.txt`: Installs all listed dependencies.

### Why it matters
- Captures the exact bill of materials required to run a Python application reliably across environments.

### How it works (internals, if relevant)
- **Direct vs Transitive Dependencies**:
  - **Direct**: Libraries your code imports directly (e.g. `requests`).
  - **Transitive**: Libraries that your direct dependencies depend on (e.g. `urllib3`, `certifi`, `idna`).
- `pip freeze` dumps both direct and transitive dependencies, which can make updating direct dependencies difficult.
- Modern tooling (`pip-tools`, `poetry`, `uv`) separates abstract top-level requirements (`requirements.in`) from locked, concrete dependency trees (`requirements.txt`).

### Common mistakes / gotchas
- Committing completely unpinned requirements (`requests` without version), which allows an unexpected breaking major release to silently break deployments.
- Committing conflicting dependency version requirements.

### Connects to
- Modern Packaging Architecture & `pyproject.toml` (subtopic 5 below).

---

## 5. Modern Packaging Architecture & `pyproject.toml`

### What it is
- The modern, declarative standard for configuring Python projects and packaging builds (PEP 517, PEP 518, PEP 621):
  - Replaces legacy files: `setup.py`, `setup.cfg`, `requirements.txt`, `MANIFEST.in`.
  - Configured via a single root file: `pyproject.toml`.
- Sections:
  - `[build-system]`: Specifies build tools (`requires = ["setuptools>=61.0"]`, `build-backend = "setuptools.build_meta"`).
  - `[project]`: Declarative project metadata (name, version, authors, dependencies, readme).
  - `[project.scripts]`: CLI console entry points.
  - `[project.optional-dependencies]`: Optional dependency groups (`dev`, `test`, `docs`).

### Why it matters
- Decouples build backends (Setuptools, Flit, Hatch, Poetry) from the build frontend (`pip`, `build`).
- Eliminates security risks of arbitrary executable code in legacy `setup.py` files during dependency resolution.

### How it works (internals, if relevant)
- `pip` parses `pyproject.toml` to identify the required build tool, creates an isolated build environment, compiles the package, and produces distribution archives.

### Common mistakes / gotchas
- Omitting the `[build-system]` table, forcing modern build tools to fall back to legacy heuristics.
- Hardcoding static versions in multiple places instead of using single-source versioning.

### Connects to
- Distribution Artifacts: Wheels vs Sdist (subtopic 6 below).

---

## 6. Distribution Artifacts: Wheels vs Source Distributions (sdist)

### What it is
- The two standard distribution formats published to PyPI:
  - **Source Distribution (`sdist`, `.tar.gz`)**: Contains raw source code, documentation, and build scripts.
  - **Built Wheel (`.whl`)**: A ZIP archive containing pre-built, ready-to-install code and compiled extensions, adhering to PEP 427.

### Why it matters
- Wheels install dramatically faster than source distributions because they bypass the build phase entirely.
- For packages containing C/C++ extensions (NumPy, Cryptography), binary wheels eliminate the requirement for users to install C compilers, Python development headers, or external SDKs on their machines.

### How it works (internals, if relevant)
- Wheel file naming convention: `{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`
  Example: `cryptography-41.0.0-cp311-cp311-manylinux_2_17_x86_64.whl`.
- `pip` checks the host machine's Python version, ABI, and CPU architecture, downloads the matching wheel, and extracts files directly into `site-packages`.

### Common mistakes / gotchas
- Publishing only an `sdist` for a C-extension package, causing installation failures for users who lack local C compilers.
- Building wheels without `manylinux` compatibility tags when targeting Linux.

### Connects to
- Packaging Best Practices (subtopic 7 below).

---

## 7. Packaging Best Practices & `src/` Layout

### What it is
- The canonical directory structure for professional Python libraries:
  ```text
  my_package/
  ├── pyproject.toml
  ├── README.md
  ├── LICENSE
  ├── tests/
  └── src/
      └── my_package/
          ├── __init__.py
          ├── core.py
          └── utils.py
  ```

### Why it matters
- **The `src/` Layout Advantage**:
  In a flat layout (`my_package/` in project root), running tests (`pytest`) imports the local uncompiled working directory files instead of the installed package artifact.
  The `src/` layout forces tests to install and import the actual packaged build (`pip install -e .`), preventing "works on my machine" deployment failures.

### How it works (internals, if relevant)
- Editable installs (`pip install -e .`): Creates a `.pth` file or finder hook in `site-packages` pointing to `src/my_package`, allowing code edits to take effect immediately without re-installing.

### Common mistakes / gotchas
- Using flat layout where tests inadvertently import internal development artifacts.
- Forgetting to test that package entry points (`[project.scripts]`) execute properly in clean environments.

### Connects to
- Intro to Flask (Topic 20).
