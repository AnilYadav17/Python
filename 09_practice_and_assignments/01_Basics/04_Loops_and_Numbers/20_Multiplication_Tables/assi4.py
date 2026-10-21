'''4.Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''

num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))
print("Armstrong Numbers are: ")
while num1<=num2:
    if num1 > 1 and num1 < 10:
        num1 += 1
        continue
    length = len(str(num1))
    org = num1
    sum =0
    while org>0:
        digit = org%10
        sum=sum+(digit**length)
        org=org//10
    if sum==num1:
        print(num1)
    num1+=1