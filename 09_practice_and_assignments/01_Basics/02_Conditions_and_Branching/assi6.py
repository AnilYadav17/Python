'''========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1'''


total = int(input("Enter the total amount: "))
ten_coins = total//10
x = total%(ten_coins*10)
five_coins = x//5
print("₹10 X",ten_coins,", ₹5 X",five_coins)
