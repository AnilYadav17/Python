'''2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []'''

#number and salaries from user
n = int(input("Enter number of salaries: "))
arr=[]
for i in range(n):
    x = int(input(f"salary{i+1}: "))
    arr.append(x)

#average
sum=0
for i in arr:
    sum+=i
avg = sum/n
main_avg = [int(avg)]

#above_avg
above_avg=[]
for i in arr:
    if i>avg:
        above_avg.append(i)

arr1=arr.copy()
#remove
for i in arr1[:]:
    if i<15000:
        arr1.remove(i)

if above_avg==[]:
    print(f"{arr} → Average = {main_avg}")
else:
    print(f"{arr} → Average = {main_avg}, Above Average = {above_avg}, Remainig = {arr1}")
