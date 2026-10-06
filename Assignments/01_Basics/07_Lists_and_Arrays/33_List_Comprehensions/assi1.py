'''1. First Non-Repeating Number
   ====================================================================

Scenario
An online voting system stores vote IDs in a list.
Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1
Input:
[4, 5, 1, 2, 1, 2, 4]
Output:
First Non-Repeating Number = 5

Test Case 2
Input:
[7, 7, 8, 8]
Output:
No Non-Repeating Number Found'''

#Taking input from user
n = int(input("Enter length of numbers: "))
arr=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr.append(x)

#first unique
f_unique=-1
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count==1:
        f_unique=i
        break
    else:
        break

if f_unique!=-1:
    print(f"First non-repeating number = {f_unique}")
else:
    print(f"No non-repeating number found")

