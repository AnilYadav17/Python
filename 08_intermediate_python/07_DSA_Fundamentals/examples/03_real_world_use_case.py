"""
03_real_world_use_case.py
Real-world scenarios:
1. Sliding Window Rate Limiter: counting requests within a rolling 60-second window.
2. Two-Pointer Reconciliation: merging two sorted audit logs from distributed microservices.
"""

from collections import deque
import time

class SlidingWindowRateLimiter:
    """
    Limits requests to max_requests within a rolling window_seconds.
    Uses sliding window queue to store timestamps.
    """
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.request_timestamps = deque()

    def allow_request(self, current_time: float) -> bool:
        # Slide window: evict timestamps older than (current_time - window_seconds)
        while self.request_timestamps and (current_time - self.request_timestamps[0] >= self.window_seconds):
            self.request_timestamps.popleft()

        if len(self.request_timestamps) < self.max_requests:
            self.request_timestamps.append(current_time)
            return True  # Allowed
        return False     # Rate limited


def merge_sorted_audit_logs(log_a, log_b):
    """
    Two-pointer merge: combines two sorted timestamped log sequences into
    a single sorted stream in O(m + n) time and O(1) auxiliary space (generator).
    """
    i, j = 0, 0
    len_a, len_b = len(log_a), len(log_b)
    merged = []

    while i < len_a and j < len_b:
        # Compare timestamp at pointers
        if log_a[i]["timestamp"] <= log_b[j]["timestamp"]:
            merged.append(log_a[i])
            i += 1
        else:
            merged.append(log_b[j])
            j += 1

    # Append remaining items
    while i < len_a:
        merged.append(log_a[i])
        i += 1
    while j < len_b:
        merged.append(log_b[j])
        j += 1

    return merged


def main():
    print("--- 1. Sliding Window Rate Limiter ---")
    limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=10.0)
    simulated_requests = [1.0, 2.5, 4.0, 5.0, 11.5, 12.0]

    for t in simulated_requests:
        allowed = limiter.allow_request(t)
        status = "ALLOWED" if allowed else "BLOCKED (429 Too Many Requests)"
        print(f"Request at t={t:4.1f}s -> {status}")

    print("\n--- 2. Two-Pointer Audit Log Merge ---")
    service_a_logs = [
        {"timestamp": 100, "event": "Auth: Login"},
        {"timestamp": 105, "event": "Cart: AddItem"},
        {"timestamp": 120, "event": "Checkout: Init"}
    ]
    service_b_logs = [
        {"timestamp": 102, "event": "Metrics: Ping"},
        {"timestamp": 108, "event": "Payment: Authorized"},
        {"timestamp": 125, "event": "Email: ReceiptSent"}
    ]

    merged_log = merge_sorted_audit_logs(service_a_logs, service_b_logs)
    for entry in merged_log:
        print(f"  [t={entry['timestamp']}] {entry['event']}")

if __name__ == "__main__":
    main()
