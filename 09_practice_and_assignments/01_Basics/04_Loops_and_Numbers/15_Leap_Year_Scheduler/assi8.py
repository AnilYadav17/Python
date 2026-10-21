'''8.Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number'''

num = int(input("Enter Number = "))
size = len(str(num))
cube = num**3

if cube%(10**size)==num:
  print("Trimorphic Number")
else:
  print("Not Trimorphic Number")
