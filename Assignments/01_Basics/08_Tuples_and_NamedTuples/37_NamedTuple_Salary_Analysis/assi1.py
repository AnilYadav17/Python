'''=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000'''

from collections import namedtuple
Emp = namedtuple("Details",["emp_id","emp_name","department","salary"])
n = int(input("Enter number of Employees: "))

Employees=[]
for i in range(n):
    print(f"Enter Employee{i+1} details: ")
    id=int(input("Enter Employee ID: "))
    name=input("Enter Employee Name: ")
    d=input("Enter Employee Department: ")
    s=float(input("Enter Employee Salary: "))
    Employees.append(Emp(id,name,d,s))

target = input("Enter Department Name: ").lower()

high_salary=Employees[0]
lowest_salary=Employees[0]
for i in range(len(Employees)):
    if Employees[i].salary>high_salary.salary:
        high_salary=Employees[i]
    elif Employees[i].salary<lowest_salary.salary:
        lowest_salary=Employees[i]
all_Sum=0
for i in range(len(Employees)):
    all_Sum+=Employees[i].salary

for i in Employees:
    print(*i)
print("\nHigh Salary Employee: \n",*high_salary)
print("\nLow Salary Employee: \n",*lowest_salary)
print("\nAverage Salary : \n", all_Sum/n)

print()
for i in range(len(Employees)):
    if Employees[i].department.lower()==target:
        print(*Employees[i])


