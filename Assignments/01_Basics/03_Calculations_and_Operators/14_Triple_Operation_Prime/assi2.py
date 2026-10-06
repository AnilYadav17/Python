'''2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime'''

import math
sum=0
product=1

n = input("Enter Number = ")
for i in n:
    sum+=int(i)
    product*=int(i)
print("Sum =",sum)
print("Product =",product)

diff = abs(product-sum)
print("Difference =",diff)

count=0
for i in str(diff):
    count+=1
print("Digits =",count)

result=count+diff
print("Final Result =",result)

if result<2:
    print("Not Prime")
else:
    for i in range(2,int(math.sqrt(result))+1):
          if result%i==0:
                print("Not Prime")
                break
    else:
          print("Prime")
          
        