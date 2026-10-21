'''2.Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496'''


num1 = int(input("Enter Number1 = "))
num2 = int(input("Enter Number2 = "))

while num1<=num2:
    sum=0
    i=1
    while i<num1:
            if num1%i==0:
                sum+=i
            i+=1
    if num1==sum:
            print(num1)
    num1+=1