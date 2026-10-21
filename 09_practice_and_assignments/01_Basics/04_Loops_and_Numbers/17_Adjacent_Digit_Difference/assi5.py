'''5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number'''



num = int(input("Enter Number = "))
org = num
length = len(str(num))
if length%2==0:
    first_half = int(num//10**(length/2))
    last_half = int(num%10**(length/2))
    print("First Half =",first_half)
    print("Second Half =",last_half)
    print("Sum =",first_half+last_half)
    print("Square =",(first_half+last_half)**2)
    if org==(first_half+last_half)**2:
        print("Tech Number")
    else:
        print("Non Tech Number")
else:
    print("Non Tech Number")