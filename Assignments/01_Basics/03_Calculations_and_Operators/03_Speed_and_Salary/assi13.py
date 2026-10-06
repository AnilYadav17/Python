'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0'''

principal,rate,time = map(float,input("Enter Principal, Rate, and Time: ").split())
CI = round(principal*(1+(rate/100))**time,2)
print("CI: ",CI,"\nAmount: ",CI+principal)

