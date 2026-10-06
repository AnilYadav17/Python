'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2'''

# import math
# num = int(input("Enter Number = "))

# if num<=1:
#     print("Composite Number")
# else:
#     flag=0
#     for i in range(2,int(math.sqrt(num))+1):
#         if num%i==0:
#             flag=1
#             break
# if flag==0:
#     print("Prime Number")
# else:
#     count =1
#     smallest=9
#     print("Composite Number")
#     for i in range(2,(num)+1):
#         if num%i==0:
#             count+=1
#             if num!=1 and smallest>i:
#                 smallest=i

# print("Factors Count = ",count)
# print("Smallest Factor = ",smallest)


count = 0
smallest = None
num = int(input("Enter Number = "))

if num<=1:
    print("Not a Composite Number")
    print("Factors Count = 0")
    print("Smallest Factor = None")
else:
    for i in range(1,num+1):
        if num%i==0:
            count+=1
            if i>1 and smallest is None:
                smallest = i
if count>2:
    print("Composite Number")
    print("Factors =",count)
    print("Smallest =",smallest)