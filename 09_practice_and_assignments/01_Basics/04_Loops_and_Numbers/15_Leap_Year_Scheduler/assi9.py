'''9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number'''


#import math
sum =0
num = int(input("Enter Number = "))
i=1
while i<num//2+1:
   if num%i==0:
      sum+=i
   i+=1

if sum>num:
   print("Abundant Number")
else:
   print("Not Abundant Number")
