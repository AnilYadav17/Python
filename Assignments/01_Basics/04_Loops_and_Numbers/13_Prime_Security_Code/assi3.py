'''3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number'''

import math
num = int(input("Enter Number = "))
flag=0
if num<=1:
    print("Natural Number")
else:
    i=2
    while i<=int(math.sqrt(num)):
        if num%i==0:
            flag+=1
            break
        i+=1
    if flag==0:
        print("Prime Number")
    else:
        print("Composite Number")
