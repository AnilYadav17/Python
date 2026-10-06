'''2.
Student Pass List Generator (Using List Comprehension)

A school stores student marks in a list. Generate a new list containing only the marks of students who have passed (marks ≥ 40).

Requirements
Read N and marks from user
Use List Comprehension
Create Pass List
Display Pass Count
Test Case

Input:

[25, 40, 55, 78, 30, 90]

Output:

Pass List = [40, 55, 78, 90]
Pass Count = 4 '''



n= int(input("Enter size of elements: "))
arr=[]
for i in range(n):
	arr.append(int(input(f"{i+1} Element: ")))

count=0
b=[i for i in arr if i>=40]
print(f"""Pass List = {b}
Pass Count = {len(b)}""")