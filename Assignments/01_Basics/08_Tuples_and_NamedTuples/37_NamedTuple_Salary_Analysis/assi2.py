'''=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''


from collections import namedtuple
S = namedtuple("Details",["roll_no","name","course","marks"])
n = int(input("Enter number of Students: "))

Students=[]
for i in range(n):
    print(f"Enter Student{i+1} Details: ")
    r=int(input("Enter Roll No:"))
    name=input("Enter Name: ")
    c=input("Enter Course: ")
    m=int(input("Enter Marks: "))
    Students.append(S(r,name,c,m))

Course = input("Enter Course Name: ")

Topper=Students[0]
Above_80 = 0
marks_sum=0
for i in range(len(Students)):
    if Students[i].marks>Topper.marks:
        Topper=Students[i]
    if Students[i].marks>80:
        Above_80+=1
    marks_sum+=Students[i].marks


print("\nTopper: \n",*Topper)
print(f"\n Students Above 80 : \n {Above_80}")
print(f"\n Average Marks: \n {marks_sum/n}")
print(f"\nStudents in {Course} Course: ")
for i in range(len(Students)):
    if Students[i].course==Course:
        print(*Students[i])