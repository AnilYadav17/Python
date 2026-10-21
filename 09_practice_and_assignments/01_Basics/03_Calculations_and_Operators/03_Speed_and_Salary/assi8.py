'''Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0'''

value = float(input("Enter the value in MB: "))
print(value,"MB in GB is :",round(value/1024,2))
