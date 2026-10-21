from Packages.for_add import students
from Packages.for_total import total
from Packages.for_per import percentage
from Packages.for_grade import grade
from Packages.for_max import maximum
from Packages.for_min import minimum

def result():
    print(f"""----------- RESULT CARD -----------

Name        : {students['name']}
Roll Number : {students['roll']}

Marks""")
    for i in range(len(students['marks'])):
        print(f"subject {i+1} : {students['marks'][i]}")
    print(f"""
Total Marks : {total(students['marks'])}
Percentage  : {percentage()}
Grade       : {grade(percentage())}
Highest Mark: {maximum(students['marks'])}
Lowest Mark : {minimum(students['marks'])}
""")
    