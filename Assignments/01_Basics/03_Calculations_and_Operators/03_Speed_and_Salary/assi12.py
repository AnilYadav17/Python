'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3'''


amount = int(input("Enter Total Amount :"))
hundred_notes = amount//100
x = amount- (hundred_notes*100)
fifty_notes = x//50
y = x-(fifty_notes*50)
ten_notes = y//10

print("₹100 x",hundred_notes,"\n₹50 x",fifty_notes,"\n₹10 x",ten_notes)
