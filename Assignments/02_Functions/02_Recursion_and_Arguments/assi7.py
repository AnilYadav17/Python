'''Assignment 3: Security PIN Verification (Palindrome Number)

A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

Task

Write a recursive function to reverse the given number and determine whether it is a palindrome.

Input 1
Enter PIN:
1221
Output 1
Palindrome Number
Input 2
Enter PIN:
1234
Output 2
Not a Palindrome Number'''

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + (n % 10))

pin = int(input("Enter PIN:\n"))
if pin == reverse_number(pin):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
