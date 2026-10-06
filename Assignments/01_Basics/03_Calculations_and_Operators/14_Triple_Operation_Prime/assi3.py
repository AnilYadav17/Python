'''3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked'''


num = int(input("Enter Number ="))
sum=0
for i in range(1,num//2+1):
    if num%i==0:
        sum+=i

if sum==num:
    print("Reward Unlocked!")
else:
    print("Try Again!")