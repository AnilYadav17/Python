'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750'''

hrs,mins,sec = map(int,input("Enter hours, minutes, seconds: ").split())
print("Total Seconds: ",((hrs*3600)+(mins*60)+sec))
