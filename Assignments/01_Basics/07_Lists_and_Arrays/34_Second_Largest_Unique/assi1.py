'''1.
 Second Largest Unique Number
Scenario

A sports academy stores athlete scores in a list.

Find the second largest unique score.

Requirements
Read N and list elements from user
Find second largest unique number
If not available, display a message
Test Case

Input:

[10, 20, 30, 40, 40]

Output:

Second Largest = 30
'''

n= int(input("Enter size of elements: "))
arr=[]
for i in range(n):
	arr.append(int(input(f"{i+1} Element: ")))

unique=[]
for i in arr:
	if i not in unique:
		unique.append(i)

unique.sort()
if len(unique)>1:
	print(f"Second largest element: {unique[-2]}")
else:
	 print(f"No second largest element possible")