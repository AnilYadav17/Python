'''
=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi
'''

results = {
    "Ajay": 88,
    "Ravi": 45,
    "Neha": 76,
    "Aman": 39
}

passing_marks = 50

# Note: The assignment specifies Passing Marks = 50, which means Ajay and Neha pass.
# Although the sample output lists Ravi (45) as passed, logically only marks >= 50 should pass.
# We check >= passing_marks to implement the correct program logic.
for student, marks in results.items():
    if marks >= passing_marks:
        print(student)
