'''1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern'''


num = int(input("Enter Number = "))

prev = num % 10
num = num // 10

differences = ""

while num > 0:
    digit = num % 10

    diff = abs(digit - prev)

    differences = str(diff) + " " + differences

    prev = digit
    num = num // 10

print("Differences:", differences)

# Even difference count
count = 0

for i in differences:
    if i != " ":
        if int(i) % 2 == 0:
            count += 1

print("Even Differences Count =", count)

# Maximum difference
maxi = 0

for i in differences:
    if i != " ":
        if int(i) > maxi:
            maxi = int(i)

print("Max Difference =", maxi)

# Uniform check
first = ""

for i in differences:
    if i != " ":
        first = i
        break

flag = True

for i in differences:
    if i != " ":
        if i != first:
            flag = False
            break

if flag:
    print("Uniform Difference")
else:
    print("Non-Uniform Pattern")