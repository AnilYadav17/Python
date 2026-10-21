"""
03_real_world_use_case.py
Real-world scenario: Production-grade Web Server Access Log Parser.
Demonstrates:
- Verbose regular expression compilation (re.VERBOSE / re.X) with comments
- Named capturing groups (?P<name>...)
- Extracting structured dictionaries with groupdict()
"""

import re
import json

# Sample lines from standard Common Log Format (Nginx / Apache)
RAW_LOG_ENTRIES = [
    '192.168.1.50 - frank [05/Sep/2026:10:15:32 +0000] "GET /api/v1/users?id=42 HTTP/1.1" 200 4821',
    '10.0.0.12 - - [05/Sep/2026:10:15:33 +0000] "POST /api/v1/checkout HTTP/1.1" 500 1024',
    '172.16.0.88 - admin [05/Sep/2026:10:15:35 +0000] "DELETE /api/v1/cache HTTP/1.1" 204 0',
]

# Verbose regex pattern with self-documenting named groups
LOG_PATTERN = re.compile(
    r"""
    ^
    (?P<client_ip>\d{1,3}(?:\.\d{1,3}){3})      # Client IP address
    \s+ - \s+
    (?P<auth_user>\S+)                         # Authenticated user or '-'
    \s+
    \[(?P<timestamp>[^\]]+)\]                  # Bracketed timestamp
    \s+
    "(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+(?P<protocol>[^"]+)" # HTTP Request line
    \s+
    (?P<status_code>\d{3})                     # 3-digit HTTP status
    \s+
    (?P<bytes_sent>\d+)                        # Body bytes sent
    $
    """,
    re.VERBOSE
)

def parse_access_logs(logs):
    parsed_records = []
    for line in logs:
        match = LOG_PATTERN.match(line.strip())
        if match:
            record = match.groupdict()
            # Type conversions for analytics
            record["status_code"] = int(record["status_code"])
            record["bytes_sent"] = int(record["bytes_sent"])
            parsed_records.append(record)
        else:
            print(f"Warning: Malformed line skipped: '{line}'")
    return parsed_records


def main():
    print("--- Real-World Access Log Parser via Named Regex Groups ---")
    parsed = parse_access_logs(RAW_LOG_ENTRIES)
    print(f"Successfully parsed {len(parsed)} structured log records:\n")
    print(json.dumps(parsed, indent=2))

if __name__ == "__main__":
    main()
