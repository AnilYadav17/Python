'''1.
Student Registration System – Longest Name

A school is organizing an inter-school cultural event. During the registration process, the coordinator notices that some students have very long names, which may not fit properly on the printed ID cards.

As a software developer, your task is to write a Python program that identifies the student with the longest name from the list of registered students using the reduce() function along with a lambda expression.

Input
students = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]
Expected Output
Student with the longest name: Christopher'''

from functools import reduce

n = int(input("Enter number of Students: "))
students = []
for i in range(n):
    students.append(input("Enter name: "))

ans = reduce(lambda a, b: a if len(a) > len(b) else b, students)
print("Student with the longest name:", ans)