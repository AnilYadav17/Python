'''2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5'''


n = int(input("Enter length of values: "))
arr=[]

for i in range(n):
    x=int(input(f"{i+1} Traffic value: "))
    arr.append(x)
arr1= arr.copy()

peak_index=[]
for i in range(n):
    if i==0:
        if n==1 or arr1[i]>=arr1[i+1]:
            peak_index.append(arr1[i])
    elif i==n-1:
        if arr1[i]>=arr1[i-1]:
            peak_index.append(arr1[i])
    else:
        if arr1[i]>=arr1[i-1] and arr1[i]>=arr1[i+1]:
            peak_index.append(arr1[i])

#sum 
sum=0
for i in peak_index:
    sum+=i

#product 
product=1
for i in peak_index:
    product*=i

#max peak
max_peak=peak_index[0]
for i in peak_index:
    if i>max_peak:
        max_peak=i

#print
print(f"""
Original array  = {arr}
Peaks = {peak_index}
Sum = {sum}
Product = {product}
Max peak = {max_peak}
""")