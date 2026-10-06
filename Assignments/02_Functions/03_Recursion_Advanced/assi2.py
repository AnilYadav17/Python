'''2.
Hospital Management System – Oldest Patient

A hospital wants to give priority to the oldest patient during a free health check-up camp. The patient details are stored as tuples containing the patient's name and age.

As a Python developer, write a program to identify the oldest patient using the reduce() function with a lambda expression.

Input
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]
Expected Output
Oldest Patient: Kiran'''

from functools import reduce

n = int(input("Enter number of Patients: "))
patients = []
for i in range(n):
    name = input(f"Enter {i+1} Name: ")
    age = int(input(f"Enter {i+1} Age: "))
    patients.append((name, age))

ans = reduce(lambda a, b: a if a[1] > b[1] else b, patients)
print("Oldest Patient:", ans[0])
