'''5.
Given an unsorted array arr[] of size N having both negative and positive integers. 
The task is place all negative element at the end of array without changing the order of positive element and negative element.

Example 1:
Input : 
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 
1  3  2  11  6  -1  -7  -5

Example 2:
Input : 
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1'''

n = int(input("Enter size of values: "))
arr=[]

for i in range(n):
    x=int(input(f"{i+1} Energy value: "))
    arr.append(x)

#copy
arr1= arr.copy()

#positive and negative numbers
positive=[]
negative=[]
for i in arr1:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)

print(positive+negative)