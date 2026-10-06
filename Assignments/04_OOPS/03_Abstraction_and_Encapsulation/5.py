# Assignment 5: Employee Salary

class Employee:
    def calculateSalary(self):
        print("Base salary calculation for Employee.")

class Manager(Employee):
    def calculateSalary(self):
        base_salary = 50000
        bonus = 10000
        print(f"Manager salary: {base_salary + bonus}")

class Developer(Employee):
    def calculateSalary(self):
        hours = 160
        rate = 300
        print(f"Developer salary: {hours * rate}")

if __name__ == "__main__":
    Employee().calculateSalary()
    Manager().calculateSalary()
    Developer().calculateSalary()
