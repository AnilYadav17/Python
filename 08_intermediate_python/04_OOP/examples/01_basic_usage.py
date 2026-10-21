"""
01_basic_usage.py
Demonstrates core OOP principles:
- Class definitions, instance attributes vs class attributes
- Instance methods, class methods (@classmethod), static methods (@staticmethod)
- Encapsulation using @property getter, setter, and validation
"""

class BankAccount:
    # Class attribute: shared configuration across all accounts
    INTEREST_RATE = 0.03
    _total_accounts = 0

    def __init__(self, owner_name, initial_balance=0.0):
        # Instance attributes: unique to each account instance
        self.owner = owner_name
        self._balance = float(initial_balance)  # Protected backing attribute
        BankAccount._total_accounts += 1

    # Property Getter: provides read access with attribute-like syntax
    @property
    def balance(self):
        return self._balance

    # Property Setter: enforces validation before mutating internal state
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Account balance cannot be negative!")
        self._balance = float(new_balance)

    # Instance Method: operates on self and can modify instance state
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    # Class Method: acts as an alternative constructor
    @classmethod
    def from_csv_row(cls, csv_string):
        """Alternative constructor: instantiates BankAccount from a 'Name,Balance' string."""
        name, balance_str = csv_string.strip().split(",")
        return cls(name.strip(), float(balance_str.strip()))

    @classmethod
    def get_total_accounts(cls):
        return cls._total_accounts

    # Static Method: independent utility bound to the class namespace
    @staticmethod
    def calculate_compound_interest(principal, rate, years):
        """Calculates compound interest without needing instance or class state."""
        return round(principal * ((1 + rate) ** years), 2)


def main():
    print("--- 1. Creating Bank Accounts ---")
    account1 = BankAccount("Alice", 1000.0)
    print(f"Created account for {account1.owner}, Balance: ${account1.balance:.2f}")

    account1.deposit(500.0)
    print(f"After deposit: ${account1.balance:.2f}")

    print("\n--- 2. Property Validation ---")
    account1.balance = 2000.0  # Uses setter
    print(f"Updated balance: ${account1.balance:.2f}")
    try:
        account1.balance = -100.0  # Should trigger ValueError
    except ValueError as err:
        print(f"Validation caught negative balance assignment: {err}")

    print("\n--- 3. Class Method as Alternative Constructor ---")
    account2 = BankAccount.from_csv_row("Bob Smith, 750.50")
    print(f"Created from CSV: {account2.owner}, Balance: ${account2.balance:.2f}")
    print(f"Total Bank Accounts Created: {BankAccount.get_total_accounts()}")

    print("\n--- 4. Static Method Utility ---")
    projected = BankAccount.calculate_compound_interest(1000, BankAccount.INTEREST_RATE, 5)
    print(f"Projected $1000 after 5 years at 3% interest: ${projected}")

if __name__ == "__main__":
    main()
