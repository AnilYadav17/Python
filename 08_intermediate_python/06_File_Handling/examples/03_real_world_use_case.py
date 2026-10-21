"""
03_real_world_use_case.py
Real-world scenario: ETL Pipeline.
Reads employee data from CSV, validates records, computes departmental salary statistics,
and generates an executive JSON report using pathlib.Path.
"""

import csv
import json
import tempfile
from pathlib import Path
from collections import defaultdict

# Sample raw CSV data
RAW_CSV_CONTENT = """id,name,department,salary
101,Alice Johnson,Engineering,125000
102,Bob Smith,Marketing,85000
103,Charlie Brown,Engineering,140000
104,Diana Prince,Product,115000
105,Evan Wright,Marketing,92000
106,Fiona Gallagher,Engineering,130000
"""

def run_etl_pipeline(input_csv: Path, output_json: Path):
    department_salaries = defaultdict(list)
    total_payroll = 0
    employee_count = 0

    # 1. Ingest CSV with DictReader
    with open(input_csv, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            salary = float(row["salary"])
            dept = row["department"]

            department_salaries[dept].append(salary)
            total_payroll += salary
            employee_count += 1

    # 2. Transform & Aggregate
    department_analytics = {}
    for dept, salaries in department_salaries.items():
        department_analytics[dept] = {
            "headcount": len(salaries),
            "average_salary": round(sum(salaries) / len(salaries), 2),
            "min_salary": min(salaries),
            "max_salary": max(salaries)
        }

    report = {
        "report_metadata": {
            "total_employees": employee_count,
            "total_payroll": total_payroll,
            "company_average_salary": round(total_payroll / employee_count, 2)
        },
        "department_breakdown": department_analytics
    }

    # 3. Export to JSON
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    return report


def main():
    with tempfile.TemporaryDirectory() as tmp_dir:
        base = Path(tmp_dir)
        csv_file = base / "employees.csv"
        json_file = base / "salary_report.json"

        # Create input CSV
        csv_file.write_text(RAW_CSV_CONTENT, encoding="utf-8")

        print("Executing ETL Pipeline...")
        report = run_etl_pipeline(csv_file, json_file)

        print("\nGenerated Salary Report:")
        print(json.dumps(report, indent=2))
        print(f"\nReport written to: {json_file.name} (File exists: {json_file.exists()})")

if __name__ == "__main__":
    main()
