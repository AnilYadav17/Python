class BankBalance:
    def __init__(self,balance):
        self.__balance = balance

    def diposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        self.__balance = amount

b1 = BankBalance(10000)
b1.diposit(1000)
# print(b1.__balance)
print(b1.get_balance())
b1.withdraw(10000)
print(b1.get_balance())
