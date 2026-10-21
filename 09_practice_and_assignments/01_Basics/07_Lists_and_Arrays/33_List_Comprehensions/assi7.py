'''7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]'''


#Taking input from user
n = int(input("Enter length of numbers: "))
k = int(input("Enter key: "))
arr=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr.append(x)

rotated= arr[-k:]+arr[:-k] #[-K:] -> Gives last , [:-k] -> Gives except last
print(rotated)