'''Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage	Grade
90 and above	A
75 to 89	B
60 to 74	C
Below 60	D

Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88

Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B'''


class Student:

    def __init__(self,roll_no,name,m1,m2,m3):
        self.roll_no = roll_no
        self.name = name
        self.m1_marks = m1
        self.m2_marks = m2
        self.m3_marks = m3
        self.total_marks()
        self.display()

    def total_marks(self):
        self.total_marks = self.m1_marks + self.m2_marks + self.m3_marks
        self.percentage = round(self.total_marks / 3 , 2)
        if self.percentage >= 90:
            self.grade = "A"
        elif self.percentage >= 75:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        else:
            self.grade = "D"

    def display(self):
        print(f"""
------ Student Result ------
Roll Number      : {self.roll_no}
Student Name     : {self.name}
Total Marks      : {self.total_marks}
Percentage       : {self.percentage}
Grade            : {self.grade}
""")


roll_no = input("Enter Roll Number: ")
name = input("Enter Student Name: ")
m1 = int(input("Enter Marks in Subject 1 : "))
m2 = int(input("Enter Marks in Subject 2 : "))
m3 = int(input("Enter Marks in Subject 3 : "))


s1 = Student(roll_no,name,m1,m2,m3)
