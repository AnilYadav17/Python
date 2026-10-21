'''1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.
For every entered number, the system analyzes relationships between its digits.

Write a program to:
Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number'''



num = int(input("Enter Number = "))
num1=num
prev = num % 10
num = num // 10
sum=0
products = ""
smallest=999
while num > 0:
    digit = num % 10

    pro = digit * prev
    sum+=pro
    if smallest>pro:
        smallest=pro
    products = str(pro) + " " + products
    prev = digit
    num = num // 10

print("Products:",products)
print("Sum:",sum)
print("Smallest:",smallest)
if sum%len(str(num1))==0:
    print("Stable Number")
else:
    print("Unstable Number")