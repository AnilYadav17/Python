'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%'''

total,obtained = map(float,input("Enter total and obtained marks :").split())
print("Percentage : ",(obtained/total*100),"%",sep="")
