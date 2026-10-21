'''4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.'''

units = int(input("Enter units consumed = "))
t3 = (units-300)*10+1900
t2 = (units-100)*7+500

print(t3) if units>300 else print(t2) if units>100 else print(units*5)