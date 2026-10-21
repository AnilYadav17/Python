"""
03_real_world_use_case.py
Real-world scenario: Real-time sliding window telemetry aggregator.
Demonstrates:
- collections.deque with maxlen for fixed-capacity rolling memory
- collections.Counter for multi-metric event frequency tracking
- collections.defaultdict for organizing device telemetry
- datetime for timestamp management
- itertools for combinatoric batch processing
"""

import datetime
from collections import deque, Counter, defaultdict
import itertools

class TelemetryAggregator:
    def __init__(self, window_size=5):
        # deque with maxlen automatically drops oldest items when capacity is reached (O(1))
        self.recent_events = deque(maxlen=window_size)
        self.device_metrics = defaultdict(list)
        self.error_counter = Counter()

    def record_event(self, device_id, metric_name, value, status="OK"):
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        event = {
            "device_id": device_id,
            "metric": metric_name,
            "value": value,
            "status": status,
            "timestamp": timestamp
        }

        self.recent_events.append(event)
        self.device_metrics[device_id].append(value)
        if status != "OK":
            self.error_counter[f"{device_id}:{status}"] += 1

    def get_window_summary(self):
        return {
            "window_event_count": len(self.recent_events),
            "recent_devices": [e["device_id"] for e in self.recent_events],
            "average_values_by_device": {
                dev: round(sum(vals) / len(vals), 2)
                for dev, vals in self.device_metrics.items()
            },
            "error_distribution": dict(self.error_counter)
        }


def main():
    print("Initializing Telemetry Aggregator (sliding window size = 4)...")
    aggregator = TelemetryAggregator(window_size=4)

    # Simulated stream of telemetry events
    events = [
        ("sensor-1", "temperature", 22.4, "OK"),
        ("sensor-2", "pressure", 101.3, "OK"),
        ("sensor-1", "temperature", 23.1, "OK"),
        ("sensor-3", "voltage", 11.2, "LOW_VOLTAGE"),
        ("sensor-2", "pressure", 103.5, "OK"),
        ("sensor-1", "temperature", 24.0, "OK"),
        ("sensor-3", "voltage", 10.8, "LOW_VOLTAGE"),
    ]

    for dev, metric, val, status in events:
        aggregator.record_event(dev, metric, val, status)

    summary = aggregator.get_window_summary()
    print("\nTelemetry Window Summary:")
    print(f"Events currently in rolling window: {summary['window_event_count']}")
    print(f"Devices in rolling window: {summary['recent_devices']}")
    print("Device Historical Averages:")
    for dev, avg in summary["average_values_by_device"].items():
        print(f"  {dev}: {avg}")
    print(f"Error Counts: {summary['error_distribution']}")

if __name__ == "__main__":
    main()
