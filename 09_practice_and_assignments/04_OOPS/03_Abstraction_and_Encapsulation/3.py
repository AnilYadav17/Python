# Assignment 3: Bank Interest Rates

class Bank:
    def getInterestRate(self):
        return 0

class SBI(Bank):
    def getInterestRate(self):
        return 5

class ICICI(Bank):
    def getInterestRate(self):
        return 6

class Axis(Bank):
    def getInterestRate(self):
        return 7

if __name__ == "__main__":
    print(f"Interest rate of Bank is {Bank().getInterestRate()}%")
    print(f"Interest rate of SBI is {SBI().getInterestRate()}%")
    print(f"Interest rate of ICICI is {ICICI().getInterestRate()}%")
    print(f"Interest rate of Axis is {Axis().getInterestRate()}%")
