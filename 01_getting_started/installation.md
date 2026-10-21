# 🛠️ Python Installation & Environment Setup

Welcome to Python! Before writing your first program, you need Python installed and configured on your operating system.

Python is a versatile, high-level, interpreted programming language. For modern development, we recommend **Python 3.10 or newer** (Python 3.12+ recommended).

---

## 1. Verify If Python Is Already Installed

Open your terminal or command prompt and run:

```bash
python3 --version
```
or on Windows:
```bash
python --version
```

If you see something like `Python 3.11.x` or `Python 3.12.x`, you already have Python installed! Verify that `pip` (Python package manager) is also available:

```bash
pip3 --version
# or
pip --version
```

If Python is not installed or your version is older than Python 3.10, follow the OS-specific instructions below.

---

## 2. Installation by Operating System

### 🐧 Linux (Ubuntu / Debian)

On modern Ubuntu or Debian distributions, Python 3 is typically pre-installed. To install or update:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

Verify installation:
```bash
python3 --version
python3 -m pip --version
```

### 🍎 macOS

The cleanest way to install and maintain Python on macOS is via [Homebrew](https://brew.sh/):

```bash
# 1. Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install Python 3
brew install python
```

Verify installation:
```bash
python3 --version
```

### 🪟 Windows

1. **Option A: Official Installer (Recommended for beginners)**
   - Download the latest installer from [python.org/downloads](https://www.python.org/downloads/).
   - ⚠️ **CRITICAL STEP:** On the very first installation screen, check the box that says:  
     **`[x] Add python.exe to PATH`**  
     *(Skipping this step prevents you from running Python from PowerShell or Command Prompt).*
   - Click **Install Now**.

2. **Option B: Windows Package Manager (`winget`)**
   Open PowerShell and execute:
   ```powershell
   winget install Python.Python.3.12
   ```

3. **Verify in PowerShell:**
   ```powershell
   python --version
   pip --version
   ```

---

## 3. Recommended Code Editors

You can write Python code in any text editor, but a dedicated IDE improves productivity dramatically:

| Editor | Best For | Why Choose It |
|:---|:---|:---|
| **[Visual Studio Code](https://code.visualstudio.com/)** | General & Beginner to Pro | Free, lightweight, outstanding Python & Pylance extensions, built-in debugger and terminal. |
| **[PyCharm Community](https://www.jetbrains.com/pycharm/)** | Deep Python Projects | Dedicated Python IDE with excellent refactoring, virtual environment management, and inspections. |
| **Terminal / CLI (`nano`, `vim`)** | Quick Edits & Servers | Available on every Linux/macOS machine. |

### Setting up VS Code for Python
1. Download and install [VS Code](https://code.visualstudio.com/).
2. Open VS Code and open the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
3. Search for and install the **Python** extension (by Microsoft).
4. Open any `.py` file—VS Code will automatically detect your Python interpreter in the bottom-right status bar.

---

## 4. Next Step

Now that your environment is ready, learn how to execute code and use the interactive shell in [Running Python](./running_python.md), or write your [First Program](./first_program.py)!
