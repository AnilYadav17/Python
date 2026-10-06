# ASSIGNMENT 2: Employee Payroll Management System (Method Overriding + Menu Driven)

class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def calculate_salary(self):
        return 0

    def display(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, monthly_salary, bonus):
        super().__init__(emp_id, name, department)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus

    def display(self):
        super().display()
        print(f"Monthly Salary : {self.monthly_salary}")
        print(f"Bonus : {self.bonus}")
        print(f"Total Salary : ₹{int(self.calculate_salary())}")

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, hourly_rate, hours_worked):
        super().__init__(emp_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display(self):
        super().display()
        print(f"Hourly Rate : {int(self.hourly_rate)}")
        print(f"Hours Worked : {int(self.hours_worked)}")
        print(f"Total Salary : ₹{int(self.calculate_salary())}")

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, department, project_name, contract_amount):
        super().__init__(emp_id, name, department)
        self.project_name = project_name
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount

    def display(self):
        super().display()
        print(f"Project Name : {self.project_name}")
        print(f"Contract Amount : {self.contract_amount}")
        print(f"Total Salary : ₹{int(self.calculate_salary())}")

if __name__ == "__main__":
    employees = []
    while True:
        print("\n========== Payroll System ==========")
        print("1. Add Full Time Employee")
        print("2. Add Part Time Employee")
        print("3. Add Contract Employee")
        print("4. Display Full Time Salary")
        print("5. Display Part Time Salary")
        print("6. Display Contract Salary")
        print("7. Exit")
        
        choice = input("Choice : ")
        
        if choice == '1':
            emp_id = input("\nEmployee ID : ")
            name = input("Name : ")
            dept = input("Department : ")
            salary = float(input("Monthly Salary : "))
            bonus = float(input("Bonus : "))
            emp = FullTimeEmployee(emp_id, name, dept, salary, bonus)
            employees.append(emp)
            print("Employee Added Successfully")
        elif choice == '2':
            emp_id = input("\nEmployee ID : ")
            name = input("Name : ")
            dept = input("Department : ")
            rate = float(input("\nHourly Rate : "))
            hours = float(input("Hours Worked : "))
            emp = PartTimeEmployee(emp_id, name, dept, rate, hours)
            employees.append(emp)
            print("Employee Added Successfully\n")
            emp.display()
        elif choice == '3':
            emp_id = input("\nEmployee ID : ")
            name = input("Name : ")
            dept = input("Department : ")
            project = input("Project Name : ")
            amount = float(input("Contract Amount : "))
            emp = ContractEmployee(emp_id, name, dept, project, amount)
            employees.append(emp)
            print("Employee Added Successfully")
        elif choice == '4':
            for emp in employees:
                if isinstance(emp, FullTimeEmployee):
                    print()
                    emp.display()
        elif choice == '5':
            for emp in employees:
                if isinstance(emp, PartTimeEmployee):
                    print()
                    emp.display()
        elif choice == '6':
            for emp in employees:
                if isinstance(emp, ContractEmployee):
                    print()
                    emp.display()
        elif choice == '7':
            break
