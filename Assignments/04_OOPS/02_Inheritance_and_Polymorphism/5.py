# ASSIGNMENT 5: School ERP System (Hierarchical Inheritance)

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Address : {self.address}\n")

class Student(Person):
    def __init__(self, name, age, address, roll_number, course, marks):
        super().__init__(name, age, address)
        self.roll_number = roll_number
        self.course = course
        self.marks = marks

    def display(self):
        print("----------- Student Details -----------\n")
        print(f"Roll Number : {self.roll_number}")
        super().display()
        print(f"Course : {self.course}")
        print(f"Marks : {self.marks}")

class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def display(self):
        print("----------- Teacher Details -----------\n")
        print(f"Employee ID : {self.employee_id}")
        super().display()
        print(f"Subject : {self.subject}")
        print(f"Salary : {self.salary}")

class Principal(Person):
    def __init__(self, name, age, address, office_number, experience, qualification):
        super().__init__(name, age, address)
        self.office_number = office_number
        self.experience = experience
        self.qualification = qualification

    def display(self):
        print("----------- Principal Details -----------\n")
        print(f"Office Number : {self.office_number}")
        super().display()
        print(f"Experience : {self.experience} Years")
        print(f"Qualification : {self.qualification}")

if __name__ == "__main__":
    people = []
    while True:
        print("\n========== School ERP ==========")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Principal")
        print("4. Display Student")
        print("5. Display Teacher")
        print("6. Display Principal")
        print("7. Exit")
        
        choice = input("Choice : ")
        
        if choice == '1':
            roll = input("\nRoll Number : ")
            name = input("Name : ")
            age = input("Age : ")
            address = input("Address : ")
            course = input("\nCourse : ")
            marks = input("Marks : ")
            student = Student(name, age, address, roll, course, marks)
            people.append(student)
            print()
            student.display()
        elif choice == '2':
            emp_id = input("\nEmployee ID : ")
            name = input("Name : ")
            age = input("Age : ")
            address = input("Address : ")
            subject = input("\nSubject : ")
            salary = input("Salary : ")
            teacher = Teacher(name, age, address, emp_id, subject, salary)
            people.append(teacher)
            print()
            teacher.display()
        elif choice == '3':
            office = input("\nOffice Number : ")
            name = input("Name : ")
            age = input("Age : ")
            address = input("Address : ")
            exp = input("\nExperience : ")
            qual = input("Qualification : ")
            principal = Principal(name, age, address, office, exp, qual)
            people.append(principal)
            print()
            principal.display()
        elif choice == '4':
            for p in people:
                if isinstance(p, Student):
                    print()
                    p.display()
        elif choice == '5':
            for p in people:
                if isinstance(p, Teacher):
                    print()
                    p.display()
        elif choice == '6':
            for p in people:
                if isinstance(p, Principal):
                    print()
                    p.display()
        elif choice == '7':
            break
