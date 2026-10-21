# 🤝 Contributing to Python Learning Hub

Thank you for your interest in contributing! Whether you are fixing a typo, improving code comments, adding an edge-case test, or contributing a new learning example, your help is welcome.

---

## 📌 Code of Conduct

* Be welcoming, respectful, and constructive.
* Keep explanations beginner-friendly and accurate.
* Respect that this repository represents an authentic learning journey—clarity and pedagogy always come before unnecessary complexity.

---

## 🎯 How You Can Contribute

1. **Fixing Typos or Clarifying Explanations:**
   Improve README files, markdown summaries, docstrings, or comments.
2. **Standardizing Code:**
   Ensure examples adhere to PEP 8 style, use meaningful variable names, and include sample input/output.
3. **Adding Edge Cases & Tests:**
   Add realistic test cases or edge cases to existing tutorial scripts.
4. **Documenting Practice Problems:**
   Add explanations or time/space complexity analysis to practice questions and LeetCode solutions.

---

## 🛠️ Contribution Workflow

1. **Fork the Repository:**
   Fork the repo on GitHub and clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/Python.git
   cd Python
   ```

2. **Create a Feature Branch:**
   ```bash
   git checkout -b feature/topic-improvement
   ```

3. **Adhere to Code Standards:**
   - **Language:** Python 3.10+ compatible syntax.
   - **Style:** Follow [PEP 8](https://peps.python.org/pep-0008/).
   - **Standard Library First:** Avoid introducing third-party dependencies for fundamental concepts.
   - **Naming Conventions:**
     - Directories: lowercase `snake_case` or numbered prefixes (e.g., `01_variables/`).
     - Python scripts: lowercase `snake_case.py` (e.g., `merge_sorted_lists.py`).
     - Avoid ambiguous filenames like `test.py`, `1.py`, or `temp.py`.
   - **Code Structure:**
     Every educational script should include:
     - A concise module docstring explaining the concept.
     - Clear, self-explanatory variable names.
     - Comments explaining non-obvious logic.
     - A runnable `if __name__ == "__main__":` entrypoint with sample output.

4. **Verify Syntax Before Committing:**
   ```bash
   python3 -m py_compile path/to/your_script.py
   ```

5. **Commit and Push:**
   Write clear, conventional commit messages:
   ```bash
   git commit -m "docs(fundamentals): clarify loop else behavior and add examples"
   git push origin feature/topic-improvement
   ```

6. **Open a Pull Request:**
   Submit a PR against the `main` branch with a clear description of changes made.

---

## ❓ Questions or Suggestions?

Open an issue on GitHub to discuss proposed changes or improvements!
