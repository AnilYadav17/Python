'''3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3'''


#Taking input from userlen(arr)
n = int(input("Enter length of numbers: "))
arr=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr.append(x)


#missing
missing=-1
for i in range(len(arr)):
    if i==0:
        if arr[i]!=1:
            missing=1
            break
    elif i==n:
        if arr[i]!=arr[i-1]+1:
            missing=arr[i-1]+1
            break

    else:
        if arr[i]!=arr[i-1]+1:
            missing=arr[i-1]+1
            break

print(f"Missing number = {missing}")