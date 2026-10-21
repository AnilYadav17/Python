'''1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3'''


#length and elements from user
n = int(input("Enter number of elements: "))
arr=[]
for i in range(n):
    x = int(input(f"Mark{i+1}: "))
    arr.append(x)

#highest
max=arr[0]
for i in arr:
    if i>max:
        max=i

#lowest
min=arr[0]
for i in arr:
    if i<min:
        min=i

#count above 75
count=0
for i in arr:
    if i>75:
        count+=1

print(f"List :→ {arr} → Highest = {max}, Lowest = {min}, Count Above 75 = {count}")

