"""
04_common_mistakes_and_fixes.py
Demonstrates common virtual environment and packaging pitfalls:
1. Committing .venv/ to version control vs .gitignore
2. Unpinned dependency catastrophe
3. PEP 668 externally-managed environment protection
"""

def mistake_1_committing_venv():
    print("--- 1. Committing .venv to Version Control ---")
    # PITFALL: Committing .venv to Git bloats repository by hundreds of MB
    # and fails on other machines because binaries are platform-dependent!
    # FIX: Always add .venv to .gitignore
    gitignore_entry = ".venv/\n__pycache__/\n*.pyc\n*.egg-info/\ndist/\nbuild/"
    print("Essential .gitignore template:\n" + gitignore_entry)


def mistake_2_unpinned_dependencies():
    print("\n--- 2. Unpinned vs Pinned Dependencies ---")
    # Unpinned: 'flask' -> May install Flask 2.x today and Flask 3.x tomorrow, breaking production!
    # Compatible pin: 'flask~=3.0.0' -> Allows 3.0.1, 3.0.2 (bug fixes), but blocks 3.1 or 4.0 (breaking changes).
    print("Best Practice: Use compatible release operator ~= or lockfiles (poetry.lock, requirements.txt).")


def mistake_3_pep_668_protection():
    print("\n--- 3. PEP 668 EXTERNALLY-MANAGED Environment ---")
    # On modern Linux, 'pip install requests' outside a venv fails with:
    # error: externally-managed-environment
    # This is a deliberate safety feature to protect system Python packages!
    print("Rule: Always activate a virtual environment before running pip install.")


def main():
    mistake_1_committing_venv()
    mistake_2_unpinned_dependencies()
    mistake_3_pep_668_protection()

if __name__ == "__main__":
    main()
