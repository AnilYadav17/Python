from model.account import Account
from service.account_service import AccountService

def display_accounts():
    service = AccountService()
    accounts = service.display_all_accounts()
    print("\n--- ALL ACCOUNTS ---")
    if not accounts:
        print("No accounts found.")
    else:
        for acc in accounts:
            print(f"Acc No: {acc.account_no} | Name: {acc.holder_name} | Balance: ₹{acc.balance:} | Type: {acc.account_type}")
    print("--------------------")

def add_account():
    service = AccountService()
    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Holder Name: ").strip()
    balance = float(input("Enter Balance: "))
    acc_type = input("Enter Account Type (Savings/Current): ").strip()        
    rows = service.add_account(Account(acc_no, name, balance, acc_type))
    if rows > 0:
            print("Account created successfully.")
    else:
            print("Failed to create account.")


def update_account():
    service = AccountService()
    
    acc_no = int(input("Enter Account Number to update: "))
    name = input("Enter New Holder Name: ").strip()
    balance = float(input("Enter New Balance: "))
        
    rows = service.update_account(acc_no, name, balance)
    if rows > 0:
        print("Account updated successfully.")
    else:
        print(f"No account found with Account Number {acc_no}.")

def delete_account():
    service = AccountService()
    acc_no = int(input("Enter Account Number to delete: "))
    rows = service.delete_account(acc_no)
    if rows > 0:
        print("Account deleted successfully.")
    else:
        print(f"No account found with Account Number {acc_no}.")

def search_account():
    service = AccountService()
    acc_no = int(input("Enter Account Number to search: "))
    acc = service.search_account(acc_no)
    if acc is None:
        print(f"Account with Number {acc_no} does not exist.")
    else:
        print("\n--- Account Details ---")
        print(f"Account No : {acc.account_no}")
        print(f"Holder Name: {acc.holder_name}")
        print(f"Balance    : ₹{acc.balance:.2f}")
        print(f"Type       : {acc.account_type}")
        print("-----------------------")


while True:
        print("\n==================================")
        print("  BANK ACCOUNT MANAGEMENT SYSTEM  ")
        print("==================================")
        print("1. Create Account")
        print("2. Update Account")
        print("3. Delete Account")
        print("4. Search Account")
        print("5. Display All Accounts")
        print("0. Exit")
        
        choice = int(input("Enter your choice (0-5): ").strip())
        match choice:
            case 1:
                add_account()
            case 2:
                update_account()
            case 3:
                delete_account()
            case 4:
                search_account()
            case 5:
                display_accounts()
            case 0:
                print("Thank you for using the Bank Account Management System. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 0 and 5.")


