'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''

import math
largest=0
smallest=9
sum=0
n = input("Enter Number = ")
for i in n:
   if int(i)>largest:
      largest=int(i)
   if smallest>int(i):
      smallest = int(i)
   
print("Largest = ",largest)
print("Smallest = ",smallest)

sum=largest+smallest
print("Sum =",sum)
if sum<=1:
   print("Not Prime")
else:
   for i in range(2,int(math.sqrt(sum))+1):
      if sum%i==0:
         print("Not Prime")
         break
   else:
      print("Prime")