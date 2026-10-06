"""
1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

******** STUDENT RESULT MANAGEMENT ********

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.

"""
students={}
def add_details(name,roll,*marks):
    students["name"]=name
    students["roll"]=roll
    students["marks"]=list(marks)
    
def total(marks):
    return sum(marks)

def percentage():
    return total(students["marks"])/len(students["marks"])

def grade(marks):
    if marks>=90:
        return "A+"
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "c"
    elif marks>=50:
        return "D"
    else:
        return "Fail"
        
def maximum(marks):
    return max(marks)
    
def minimum(marks):
    return min(marks)
    
def result():
    print(f"""----------- RESULT CARD -----------

Name        : {students["name"]}
Roll Number : {students["roll"]}

Marks""")
    for i in range(len(students['marks'])):
        print(f"subject {i+1} : {students["marks"][i]}")
    print(f"""
Total Marks : {total(students["marks"])}
Percentage  : {percentage()}
Grade       : {grade(percentage())}
Highest Mark: {maximum(students["marks"])}
Lowest Mark : {minimum(students["marks"])}
""")
    

while True:
	print("""
================================
STUDENT RESULT MANAGEMENT SYSTEM
================================
MENU
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
""")
	choice = int(input("Enter Choice: "))
	match choice:
		case 1:
			name = input("Enter Student Name : ")
			roll = int(input("Enter Roll Number : "))
			n = int(input("Enter number of Subjects: "))
			marks=[]
			for i in range(n):
				marks.append(int(input(f"Enter Mark {i+1} :")))
			
			add_details(name,roll,*marks)

		case 2:
		    print(f"Total Marks : {total(students["marks"])}")
		    
		case 3:
		    print(f"Total Percentage : {percentage()}")
		    
		case 4:
		    print(f"Grade : {grade(percentage())}")
		    
		case 5:
		    result()
		    
		case 6:
		    print(f"Highest Mark: {maximum(students["marks"])}")
		
		case 7:
		    print(f"Lowest Mark : {minimum(students["marks"])}")
		    
		case 8:
		    print("Thank You. Program Terminated.")
		    break
		    
		case _:
			print("Enter a valid choice!")
