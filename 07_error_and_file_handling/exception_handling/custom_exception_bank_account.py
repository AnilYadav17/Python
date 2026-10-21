class InsufficientBalane(Exception):
    pass

class NegativeDepositException(Exception):
    pass

class BankAccount:
    def __init__(self,actnumber,acholder,balance):
        self.actnumber = actnumber
        self.acholder = acholder
        self.balance = balance

    def deposit(self,amount):
        if amount<0:
            raise NegativeDepositException("Deposit amount can not be negative!")
        self.balance = self.balance + amount
        print(f"Deposit successful\nCurrent Balance:",self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalane("Insufficient balance!")
        self.balance = self.balance - amount
        print(f"Withdraw successful\nCurrent Balance:",self.balance)

actnumber = int(input("Enter Account Number: "))
acholder = input("Enter Holder Name: ")
balance = int(input("Enter Balance: "))

acc = BankAccount(actnumber, acholder ,balance)

#Deposit
try:
    amount = float(input("Enter Deposit amount: "))
    acc.deposit(amount)
except NegativeDepositException as n:
    print("Negative Deposit:",n)


#Withdraw
try:
    amount = float(input("Enter withdraw amount: "))
    acc.withdraw(amount)
except InsufficientBalane as i:
        print("Insufficient Balance:",i)