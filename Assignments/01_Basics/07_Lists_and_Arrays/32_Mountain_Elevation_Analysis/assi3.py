'''3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1925
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0'''


n = int(input("Enter size of values: "))
arr=[]

for i in range(n):
    x=int(input(f"{i+1} Energy value: "))
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

#sum of squares
squares_sum=0
for i in peak_index:
    squares_sum+=i**2

#average
sum=0
count=0
for i in peak_index:
    sum+=i
    count+=1
average=int(sum/count)

#difference
max_peak=peak_index[0]
min_peak=peak_index[0]
for i in peak_index:
    if i>max_peak:
        max_peak=i
    if i<min_peak:
        min_peak=i
difference = abs(max_peak - min_peak)

#print
print(f"""
Original array  = {arr}
Peaks = {peak_index}
Sum of squares = {squares_sum}
Average = {average}
Difference = {difference}
""")