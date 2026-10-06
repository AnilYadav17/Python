'''5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome'''

n = int(input("Enter Number = "))
rev = 0
org=n

while n>0:
 digit=n%10
 rev = rev*10+digit
 n = n//10

if  org==rev:
    print("Polindrome")
else:
    print("Not Polindrome")
