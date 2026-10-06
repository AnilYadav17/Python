# Problem 1: Loyalty Points System

class Customer:
    def calculateLoyaltyPoints(self, amount):
        return amount // 10

class PremiumCustomer(Customer):
    def calculateLoyaltyPoints(self, amount):
        return 2 * (amount // 10)

if __name__ == "__main__":
    amount = int(input())
    premium = input().strip().lower()
    
    if premium == "yes":
        customer = PremiumCustomer()
    else:
        customer = Customer()
        
    print(customer.calculateLoyaltyPoints(amount))
