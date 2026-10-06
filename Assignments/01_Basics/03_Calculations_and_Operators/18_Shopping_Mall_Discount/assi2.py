'''2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.'''

marks = int(input("Enter Marks = "))
print("A+") if marks>=90 else print("A") if marks>=75 else print("B") if marks>=60 else print("C") if marks>=50 else print("Fail") 