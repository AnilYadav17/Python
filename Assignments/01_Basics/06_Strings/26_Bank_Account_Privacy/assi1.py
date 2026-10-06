'''1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ********9012'''
number = input("Enter account number: ")

first_result = ""
second_result = ""

length = len(number)

if length == 12:

    # masking part
    for i in range(length - 4):
        first_result = first_result + "*"

    # last 4 digits
    for j in range(length - 4, length):
        second_result = second_result + number[j]

    print("Masked Account:", first_result + second_result)

else:
    print("Please enter valid account number")