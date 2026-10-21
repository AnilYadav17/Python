"""
03_real_world_use_case.py
Real-world scenario: Pluggable notification service architecture.
Demonstrates:
- Abstract Base Classes (ABCs) enforcing interface contracts
- Composition over inheritance
- Duck typing and polymorphic dispatch
"""

import abc

# 1. Abstract Base Class enforcing the Notification Channel contract
class NotificationChannel(abc.ABC):
    @abc.abstractmethod
    def send(self, recipient, message):
        """Subclasses MUST implement send(recipient, message)."""
        pass

    @property
    @abc.abstractmethod
    def channel_name(self):
        """Subclasses MUST define channel_name."""
        pass


# 2. Concrete implementations
class EmailChannel(NotificationChannel):
    @property
    def channel_name(self):
        return "Email"

    def send(self, recipient, message):
        # Simulated email delivery
        return f"[Email Sent] To: <{recipient}> Body: '{message}'"


class SlackChannel(NotificationChannel):
    def __init__(self, webhook_url="https://hooks.slack.com/services/..."):
        self.webhook = webhook_url

    @property
    def channel_name(self):
        return "Slack"

    def send(self, recipient, message):
        # Simulated Slack webhook post
        return f"[Slack Notification] Channel: #{recipient} Message: '{message}'"


class SMSChannel(NotificationChannel):
    @property
    def channel_name(self):
        return "SMS"

    def send(self, recipient, message):
        # Simulated SMS transmission
        return f"[SMS Sent] Number: {recipient} Text: '{message}'"


# 3. Composite Service using Dependency Injection
class AlertService:
    """
    AlertService does NOT inherit from notification channels.
    It COMPOSES a list of channels and delegates dispatching to them.
    """
    def __init__(self, channels=None):
        # Store list of channels
        self.channels = list(channels) if channels else []

    def register_channel(self, channel: NotificationChannel):
        if not isinstance(channel, NotificationChannel):
            raise TypeError("Channel must implement NotificationChannel interface.")
        self.channels.append(channel)

    def broadcast_alert(self, recipient_map, message):
        """
        Polymorphically dispatches the alert to all registered channels.
        recipient_map maps channel_name to appropriate recipient destination.
        """
        results = []
        for ch in self.channels:
            if ch.channel_name in recipient_map:
                destination = recipient_map[ch.channel_name]
                dispatch_status = ch.send(destination, message)
                results.append(dispatch_status)
        return results


def main():
    print("--- Pluggable Notification System ---")
    email_channel = EmailChannel()
    slack_channel = SlackChannel()
    sms_channel = SMSChannel()

    # Compose the alert service with multiple channels
    service = AlertService([email_channel, slack_channel, sms_channel])

    recipients = {
        "Email": "admin@example.com",
        "Slack": "devops-alerts",
        "SMS": "+1-555-0199"
    }

    print("Broadcasting high-priority alert...")
    logs = service.broadcast_alert(recipients, "Database latency spike detected!")
    for log in logs:
        print(f"  {log}")

if __name__ == "__main__":
    main()
