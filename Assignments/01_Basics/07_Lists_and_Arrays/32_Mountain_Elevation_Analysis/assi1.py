'''1.
Mountain Hiking Elevation Analysis

Problem Statement

A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

Given an array elevation[] of size N, find the index of any one peak checkpoint.

Test Case 1

Input:
elevation = [1200, 1450, 1700, 1600, 1500]

Output:
2

Explanation:
1700 is greater than both adjacent values 1450 and 1600.

Test Case 2

Input:
elevation = [800, 900, 950, 1000]

Output:
3

Explanation:
Last element can also be a peak because it has no right neighbor.

Test Case 3

Input:
elevation = [3000]

Output:
0

Explanation:
Single element is always a peak.'''


n = int(input("Enter length: "))
arr=[]

for i in range(n):
    x=int(input(f"{i+1} Elevation value: "))
    arr.append(x)
arr1= arr.copy()

peak_index=-1
for i in range(n):
    if i==0:
        if n==1 or arr1[i]>=arr1[i+1]:
            peak_index=i
    elif i==n-1:
        if arr1[i]>=arr1[i-1]:
            peak_index=i
    else:
        if arr1[i]>=arr1[i-1] and arr1[i]>=arr1[i+1]:
            peak_index=i

if i!=-1:
    print(f"First peak index: {peak_index}")
else:
    print("No peak index found!")