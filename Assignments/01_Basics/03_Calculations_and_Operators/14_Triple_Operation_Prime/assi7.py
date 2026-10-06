'''7.Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime'''

x = 0
num = input("Enter Number = ")
for i in num:
    if x==0:
        x = int(i)
    