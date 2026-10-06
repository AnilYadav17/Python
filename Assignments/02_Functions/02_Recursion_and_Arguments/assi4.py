'''4.
Assignment: Scholarship Eligibility System (Using filter(), map(), and sorted() with Lambda Expressions)

A university is offering scholarships to students based on their academic performance.

The scholarship committee has decided on the following rules:

Only students who score 75 marks or above are eligible for the scholarship.
Eligible students will receive 5 bonus marks to reward their outstanding performance.
Finally, the updated marks should be displayed in descending order.

As a software developer, your task is to automate this process using Python.

Note: Use filter() to select eligible students, map() to add the bonus marks, and sorted() to display the final marks in descending order. All three operations must use lambda expressions.

Task

Write a Python program that:

Filters students who have scored 75 or above.
Adds 5 bonus marks to each eligible student.
Sorts the updated marks in descending order.
Displays the final list of scholarship marks.
Input Format
The first line contains an integer N, representing the number of students.
The second line contains N space-separated marks.
Output Format

Display the updated scholarship marks in descending order.

Sample Input
Enter the number of students:
8

Enter the marks:
65 80 92 74 88 76 55 95
Sample Output
Scholarship Marks:
100 97 93 85 81'''

bonus_marks=[]
marks=[]
def add_marks():
	n = int(input("Enter number of Marks: "))
	for i in range(n):
		marks.append(int(input(f"Enter Subject{i+1} Marks: ")))
	print("Marks updated successfully.\n")

def add_bonus():
	updated_marks= map(lambda x:x+5,filter(lambda x:x>=75,marks))
	bonus_marks.extend(list(updated_marks))

def rev():
	return sorted(bonus_marks,reverse=True)


def main():
	add_marks()
	add_bonus()
	print("Scholarship Marks:\n",*rev())
	
main()
