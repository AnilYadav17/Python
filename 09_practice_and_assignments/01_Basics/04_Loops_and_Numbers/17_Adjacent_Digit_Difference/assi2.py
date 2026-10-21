'''
2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number'''

num = int(input("Enter Number = "))
length = len(str(num))
if length%2==0:
    first_half = int(num//10**(length/2))
    last_half = int(num%10**(length/2))
    sum1=0
    sum2=0
    for i in str(first_half):
        sum1+=int(i)
    for i in str(last_half):
        sum2+=int(i)
    print("First Half Sum =",sum1,"\nSecond Half Sum =",sum2)
    if sum1==sum2:
        print("Balanced Number")
    else:
        print("Unbalanced Number")

else:
    print("Unbalanced Number")

