# ASSIGNMENT 4: Banking Loan Management System (Multilevel Inheritance)

class Person:
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

class Customer(Person):
    def __init__(self, name, age, mobile, customer_id, account_number):
        super().__init__(name, age, mobile)
        self.customer_id = customer_id
        self.account_number = account_number

class LoanAccount(Customer):
    def __init__(self, name, age, mobile, customer_id, account_number, loan_amount, interest_rate, loan_tenure):
        super().__init__(name, age, mobile, customer_id, account_number)
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_tenure = loan_tenure

    def display(self):
        print("----------- Loan Details -----------\n")
        print(f"Customer Name : {self.name}")
        print(f"Customer ID : {self.customer_id}")
        print(f"Account Number : {self.account_number}\n")
        print(f"Loan Amount : ₹{int(self.loan_amount)}")
        print(f"Interest Rate : {self.interest_rate}%")
        print(f"Loan Tenure : {self.loan_tenure} Years")

if __name__ == "__main__":
    loans = []
    while True:
        print("\n1. Add Customer Loan Details")
        print("2. Display Loan Details")
        print("3. Exit")
        
        choice = input("Choice : ")
        
        if choice == '1':
            name = input("Customer Name : ")
            age = input("Age : ")
            mobile = input("Mobile : ")
            c_id = input("\nCustomer ID : ")
            acc = input("Account Number : ")
            amount = float(input("\nLoan Amount : "))
            rate = float(input("Interest Rate : "))
            tenure = int(input("Loan Tenure : "))
            loan = LoanAccount(name, age, mobile, c_id, acc, amount, rate, tenure)
            loans.append(loan)
            print()
            loan.display()
        elif choice == '2':
            for loan in loans:
                print()
                loan.display()
        elif choice == '3':
            break
