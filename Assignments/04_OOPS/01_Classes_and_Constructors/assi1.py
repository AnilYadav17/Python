'''Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0'''

class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
        self.salary_Details()
        self.display()

    def salary_Details(self):
        self.basic_salary=self.salary
        self.hra_salary = self.salary/5
        self.da_salary = self.salary*(15/100)
        self.gross_salary = self.basic_salary + self.hra_salary + self.da_salary

    def display(self):
        print(f"""
------ Employee Salary Details ------
Employee ID      : {self.id}
Employee Name    : {self.name}
Basic Salary     : {self.basic_salary}
HRA              : {self.hra_salary}
DA               : {self.da_salary}
Gross Salary     : {self.gross_salary}
""")


id = input("Enter EmployeeID: ")
name = input("Enter Employee Name: ")
salary = float(input("Enter Employee Salary: "))


e1 = Employee(id,name,salary)
