'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0'''

original_price,down_payment,interest_rate,months =  map(float,input("Enter Mobile Price , Down Payment ,Interest rate and Months: ").split())
remaining_amount = original_price - down_payment
total = remaining_amount*interest_rate/100 + remaining_amount
monthly = total/months
print("Remaining Amount:",remaining_amount,"\nTotal with Interest:",total,"\nMonthly EMI:",monthly)
