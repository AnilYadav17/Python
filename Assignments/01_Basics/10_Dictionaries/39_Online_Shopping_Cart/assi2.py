'''=========================================
EMPLOYEE DEPARTMENT COUNT
=========================

A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.

Sample Output:
{'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}'''

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]
d = {}

for i in employees:
        d[i]=d.get(i,0)+1

print(d)