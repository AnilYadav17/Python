"""
05_advanced_idiomatic.py
Demonstrates modern packaging standards with pyproject.toml:
- Writing a compliant PEP 517 / PEP 621 pyproject.toml configuration
- Validating the configuration using Python's standard library tomllib (Python 3.11+)
"""

import tomllib

SAMPLE_PYPROJECT_TOML = """
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "enterprise_data_core"
version = "1.0.0"
description = "High-performance enterprise data streaming toolkit"
readme = "README.md"
authors = [
    { name = "Core Platform Team", email = "platform@enterprise.com" }
]
license = { text = "MIT" }
requires-python = ">=3.10"
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.5.0",
    "sqlalchemy>=2.0.0"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "mypy>=1.6.0",
    "black>=23.9.0"
]

[project.scripts]
enterprise-cli = "enterprise_data_core.cli:main"
"""

def validate_pyproject_toml(toml_string: str):
    # tomllib.loads parses TOML string into a Python dictionary
    data = tomllib.loads(toml_string)

    build_system = data.get("build-system", {})
    project = data.get("project", {})

    print(f"Package Name:    {project.get('name')}")
    print(f"Package Version: {project.get('version')}")
    print(f"Python Support:  {project.get('requires-python')}")
    print(f"Build Backend:   {build_system.get('build-backend')}")
    print(f"CLI Entry Point: {project.get('project.scripts', project.get('scripts'))}")
    print(f"Direct Runtime Dependencies: {len(project.get('dependencies', []))}")
    print(f"Dev Dependencies: {len(project.get('optional-dependencies', {}).get('dev', []))}")

    return data


def main():
    print("--- Parsing & Validating pyproject.toml with tomllib ---")
    parsed = validate_pyproject_toml(SAMPLE_PYPROJECT_TOML)
    print("\nValidation Succeeded! Modern declarative configuration ready for distribution.")

if __name__ == "__main__":
    main()
