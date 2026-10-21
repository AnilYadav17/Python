'''
=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
'''

students = {
    "Ajay": 78,
    "Ravi": 92,
    "Neha": 85,
    "Aman": 65
}

highest = None
lowest = None

for name, marks in students.items():
    if highest is None or marks > students[highest]:
        highest = name
    if lowest is None or marks < students[lowest]:
        lowest = name

print("Highest Marks :", highest, students[highest])
print("Lowest Marks :", lowest, students[lowest])

