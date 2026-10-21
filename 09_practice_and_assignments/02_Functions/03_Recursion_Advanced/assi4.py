'''4.
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password'''

def check_even_digits(n):
    if n == 0:
        return True
    if (n % 10) % 2 != 0:
        return False
    return check_even_digits(n // 10)

password = int(input("Enter Password:\n"))

if password == 0 or check_even_digits(password):
    print("Strong Password")
else:
    print("Weak Password")
