'''7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''

import math
n = int(input("Enter Number = "))
sum=0

for i in str(n):
    sum = sum+int(i)
print("Sum =",sum)
if sum<=1:
   print("Not Lucky Number")
flag=0
for i in range(2,int(math.sqrt(sum))):
   if sum%i==0:
      flag+=1
      break

if flag==0:
   print("Lucky Number")
else: 
   print("Not Lucky Number")

