'''2.
 Employee Bonus Calculation (Using filter() and map() with Lambda Expressions)


A software company wants to reward its high-performing employees with a 10% bonus. However, only employees earning ₹50,000 or more are eligible for
 the bonus.

As a software developer, your task is to:

Filter the salaries of eligible employees.
Calculate the updated salary after adding a 10% bonus.
Display the final salaries of the eligible employees.

Note: Use filter() to identify eligible employees and map() to calculate the updated salaries. Both operations must use lambda expressions.

Input Format
The first line contains an integer N, representing the number of employees.
The second line contains N space-separated salary values.
Output Format

Display the updated salaries of all eligible employees after adding a 10% bonus.

Sample Input
Enter the number of employees:
6

Enter the salaries:
35000 50000 62000 45000 70000 55000
Sample Output
Eligible Employees' Updated Salaries:
55000.0 68200.0 77000.0 60500.0
'''

salaries=[]
n = int(input("Enter Number of Employees: "))
for i in range(n):
    salaries.append(int(input(f"Enter {i+1} salary: ")))
    
x = map(lambda x:x+x/10,filter(lambda x:x>=50000,salaries))

print("\nEligible Employees' Updated Salaries:\n",*list(x))
    
