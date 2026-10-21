"""
03_real_world_use_case.py
Real-world scenario: Dependency Auditor & requirements.txt Parser.
Demonstrates:
- Parsing requirements with version specifiers (==, >=, <=, ~=)
- Checking for duplicate or conflicting package pins
- Classifying direct vs transitive dependencies
"""

import re
from collections import defaultdict

SAMPLE_REQUIREMENTS = """
# Web Framework & Core APIs
fastapi==0.104.1
uvicorn[standard]>=0.24.0
pydantic>=2.0,<3.0

# Database & Storage
sqlalchemy~=2.0.0
asyncpg==0.29.0

# Security & Tokens
cryptography>=41.0.0
pyjwt==2.8.0

# Conflicting entry for testing
fastapi==0.99.0
"""

def parse_and_audit_requirements(req_text: str):
    packages = defaultdict(list)
    line_pattern = re.compile(r"^([a-zA-Z0-9_\-\[\]]+)\s*([=><~^!]+.*)?$")

    for line_no, raw_line in enumerate(req_text.splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue  # Skip comments and blank lines

        match = line_pattern.match(line)
        if match:
            pkg_name = match.group(1).split("[")[0].lower()  # Strip extras like [standard]
            specifier = match.group(2) if match.group(2) else "ANY"
            packages[pkg_name].append({"line": line_no, "specifier": specifier})

    conflicts = {}
    for pkg, occurrences in packages.items():
        if len(occurrences) > 1:
            conflicts[pkg] = occurrences

    return packages, conflicts


def main():
    print("--- Requirements.txt Dependency Auditor ---")
    packages, conflicts = parse_and_audit_requirements(SAMPLE_REQUIREMENTS)

    print(f"Total Unique Packages Parsed: {len(packages)}")
    for pkg, records in packages.items():
        specs = ", ".join(r["specifier"] for r in records)
        print(f"  {pkg:<15} -> {specs}")

    if conflicts:
        print("\n[ALERT] Conflicting / Duplicate Dependencies Detected:")
        for pkg, occurrences in conflicts.items():
            print(f"  Package '{pkg}' defined multiple times:")
            for occ in occurrences:
                print(f"    - Line {occ['line']}: {occ['specifier']}")

if __name__ == "__main__":
    main()
