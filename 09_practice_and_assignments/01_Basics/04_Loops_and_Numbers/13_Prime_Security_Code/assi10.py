'''10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0'''

import math
zero_count=0
sum=0
smallest=0
num = input("Enter Number = ")
for i in num:
    if int(i)==0:
        zero_count+=1
    sum+=int(i)
    if int(i)<smallest:
        smallest=int(i)

result = (zero_count+sum)*smallest
print("Zero Count =",zero_count)
print("Sum =",sum)
print("Smallest Digit  =",smallest)
print("Final Result  =", result)

if result<2:
    print("Not Prime")
else:
    for i in range(2,int(math.sqrt(result))+1):
        if result%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")




