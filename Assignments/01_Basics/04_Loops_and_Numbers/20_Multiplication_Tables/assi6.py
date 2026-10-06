'''6.Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''

num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))
print("Pollindrome Numbers are: ")

while num1<=num2:
    org = num1
    rev=""
    for i in str(num1):
        rev=i+rev
    if str(org)==rev:
        print(num1)
    num1+=1