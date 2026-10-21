"""
03_real_world_use_case.py
Real-world scenario: Payment processing engine with domain-specific exception hierarchy.
Demonstrates:
- Base domain exception and granular sub-exceptions
- Attaching structured metadata (transaction_id, error_code, retryable flag)
- Exception translation and error serialization for API clients
"""

import time

# 1. Base Domain Exception
class PaymentError(Exception):
    """Base exception for all payment gateway failures."""
    def __init__(self, message, error_code, retryable=False):
        super().__init__(message)
        self.error_code = error_code
        self.retryable = retryable

    def to_dict(self):
        return {
            "error_type": self.__class__.__name__,
            "message": str(self),
            "code": self.error_code,
            "retryable": self.retryable
        }


# 2. Granular Specialized Exceptions
class InsufficientFundsError(PaymentError):
    def __init__(self, requested_amount, current_balance):
        super().__init__(
            f"Insufficient funds: requested ${requested_amount:.2f}, but balance is ${current_balance:.2f}",
            error_code="INSUFFICIENT_FUNDS",
            retryable=False
        )
        self.requested = requested_amount
        self.balance = current_balance


class CardDeclinedError(PaymentError):
    def __init__(self, decline_code):
        super().__init__(
            f"Card declined by issuing bank (reason: {decline_code})",
            error_code="CARD_DECLINED",
            retryable=False
        )
        self.decline_code = decline_code


class GatewayTimeoutError(PaymentError):
    def __init__(self, gateway_name):
        super().__init__(
            f"Payment gateway '{gateway_name}' timed out after 5000ms",
            error_code="GATEWAY_TIMEOUT",
            retryable=True  # Can be retried automatically
        )


# 3. Payment Service
class PaymentGateway:
    def process_charge(self, account_balance, amount, card_status):
        if card_status == "STOLEN":
            raise CardDeclinedError("SUSPECTED_FRAUD")
        if card_status == "TIMEOUT":
            raise GatewayTimeoutError("StripeProcessor")
        if amount > account_balance:
            raise InsufficientFundsError(amount, account_balance)

        return {"transaction_id": "txn_987654321", "amount": amount, "status": "SUCCESS"}


def handle_client_checkout(balance, amount, card_status):
    gateway = PaymentGateway()
    try:
        receipt = gateway.process_charge(balance, amount, card_status)
        print(f"Checkout Success: {receipt}")
    except PaymentError as exc:
        # Uniform handling of all payment errors using domain metadata
        err_payload = exc.to_dict()
        print(f"Checkout Failed: {err_payload}")
        if exc.retryable:
            print("  -> System Action: Queuing request for background retry.")
        else:
            print("  -> System Action: Prompting user for alternative payment method.")


def main():
    print("--- 1. Successful Transaction ---")
    handle_client_checkout(500.0, 150.0, "ACTIVE")

    print("\n--- 2. Insufficient Funds Failure ---")
    handle_client_checkout(50.0, 200.0, "ACTIVE")

    print("\n--- 3. Card Declined Failure ---")
    handle_client_checkout(1000.0, 50.0, "STOLEN")

    print("\n--- 4. Gateway Timeout Failure (Retryable) ---")
    handle_client_checkout(1000.0, 50.0, "TIMEOUT")

if __name__ == "__main__":
    main()
