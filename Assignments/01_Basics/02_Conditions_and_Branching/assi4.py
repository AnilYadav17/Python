'''========================================
Assignment 4: Travel Fare Calculator
========================================

A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300'''

distance = float(input("Enter the number of kilometers traveled: "))
fare = distance*15
print("Total fare = ₹",fare,sep="")
