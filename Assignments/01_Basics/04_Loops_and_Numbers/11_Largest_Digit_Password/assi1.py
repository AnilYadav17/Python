'''1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9'''
largest=0

n = int(input("Enter Number :"))
while n>0:
    digit = n%10
    if largest<digit:
        largest=digit
    n=n//10

print("Largest Digit =",largest)



