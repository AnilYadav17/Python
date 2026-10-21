'''1.
Employee Record Sorting (Lambda)


A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

Task

Write a Python program to sort the employee records using a lambda expression.

Input
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]

'''

employee=[]
def add_employee():
    n  = int(input("Enter number of Employees: "))
    for i in range(n):
	    emp = input(f"Enter {i+1} name: ")
	    salary = int(input(f"Enter {i+1} salary: "))
	    employee.append((emp,salary))
    print("Registered Successfully\n")
    
def sort():
    return sorted(employee, key=lambda x:x[1])
    

def main():
    add_employee()
    print("Sorted by salary: \n",sort())
    
    
main()
