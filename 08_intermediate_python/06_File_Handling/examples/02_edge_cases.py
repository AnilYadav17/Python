"""
02_edge_cases.py
Demonstrates tricky file handling edge cases:
- The 'w+' vs 'r+' file mode truncation trap
- Missing newline='' in CSV operations
- JSON serialization failure on datetime / Decimal objects and its fix
"""

import json
import csv
import datetime
import tempfile
from pathlib import Path

def demonstrate_wplus_vs_rplus_trap(work_dir: Path):
    print("--- 1. 'w+' vs 'r+' Mode Truncation Trap ---")
    target = work_dir / "important_data.txt"
    target.write_text("CRITICAL SYSTEM DATA", encoding="utf-8")

    # DANGER: opening in 'w+' IMMEDIATELY truncates file to 0 bytes!
    with open(target, "w+", encoding="utf-8") as f:
        content_after_wplus = f.read()
        print(f"Content immediately after open('w+'): '{content_after_wplus}' (WIPED OUT!)")

    # SAFE: use 'r+' to read and update without truncating
    target.write_text("VERSION_1", encoding="utf-8")
    with open(target, "r+", encoding="utf-8") as f:
        original = f.read()
        f.seek(0)
        f.write("VERSION_2")
    print(f"After 'r+' in-place update: '{target.read_text(encoding='utf-8')}'")


def demonstrate_csv_newline_requirement(work_dir: Path):
    print("\n--- 2. CSV Writing: newline='' Parameter ---")
    csv_path = work_dir / "records.csv"

    # Always specify newline="" to let csv module control line endings
    rows = [["id", "name", "role"], [1, "Alice", "Admin"], [2, "Bob", "User"]]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        read_rows = list(reader)
    print(f"CSV read back correctly: {read_rows}")


def demonstrate_json_custom_serialization():
    print("\n--- 3. JSON Custom Type Serialization ---")
    payload = {
        "event": "USER_SIGNUP",
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
        "user_id": 402
    }

    # Direct json.dumps(payload) raises: TypeError: Object of type datetime is not JSON serializable

    # FIX: Provide a default serializer handler
    def custom_json_serializer(obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")

    json_str = json.dumps(payload, default=custom_json_serializer, indent=2)
    print(f"Successfully serialized custom datetime to JSON:\n{json_str}")


def main():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)
        demonstrate_wplus_vs_rplus_trap(p)
        demonstrate_csv_newline_requirement(p)
        demonstrate_json_custom_serialization()

if __name__ == "__main__":
    main()
