'''9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime'''

import math
num = input("Enter Number = ")
odd_count = 0
even_count = 0

for i in num:
    if int(i)%2==0:
        even_count+=1
    elif int(i)%2!=0:
        odd_count+=1

print("Even Count =",even_count)
print("Odd Count =",odd_count)
print("Difference =",abs(even_count-odd_count))

diff=abs(even_count-odd_count)

if diff<2:
    print("Not Prime")
else:
    for i in range(2,int(math.sqrt(diff))+1):
        if diff%int(i)==0:
            print("Not Prime")
            break
    else:
        print("Prime")

