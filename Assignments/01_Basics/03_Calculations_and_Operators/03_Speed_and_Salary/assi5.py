'''Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0'''


m1,m2,m3 = map(float,input("Enter three subject marks: ").split())
print("Average : ",((m1+m2+m3)/3))
