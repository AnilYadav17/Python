'''5.Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number'''

num = input("Enter Number = ")
square = int(num) * int(num)
digit = len(num)

if square % (10 ** digit) == int(num):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")
