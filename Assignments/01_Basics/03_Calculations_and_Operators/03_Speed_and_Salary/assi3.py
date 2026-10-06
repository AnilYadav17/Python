'''Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600'''

units = float(input("Enter the number of units: "))
print("Bill : ",units*6,"₹",sep="")
