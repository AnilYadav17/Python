'''1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.'''

amount = float(input("Enter Amount = "))
customer_type = input("Enter Customer Type(Regular or Premium) = ").lower()

print("Final Payable =",amount-(amount/5)) if customer_type=="premium" and amount>5000 else print("Final Payable =",amount-(amount/10)) if customer_type=="premium" else print("Final Payable =",amount-(amount/10)) if amount>3000 else print("Final Payable =",amount-(amount/20))