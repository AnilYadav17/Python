'''ASSIGNMENT 1: Hospital Management System (Single Inheritance)

Scenario

A software company has been hired to develop a Hospital Management System. Every person associated with the hospital has some common details, but each category has its own unique information.

Create a base class Person containing:

Person ID

Name

Age

Mobile Number

Create the following derived classes:

Doctor

Specialization

Experience (Years)

Consultation Fee

Nurse

Department

Shift (Day/Night)

Salary

Patient

Disease

Ward Number

Bill Amount

Functional Requirements

Create a menu-driven application.

========== Hospital Management ==========

1. Add Doctor

2. Add Nurse

3. Add Patient

4. Display Doctor Details

5. Display Nurse Details

6. Display Patient Details

7. Exit

Sample Input

Enter Choice : 1



Enter Doctor ID : 101

Enter Name : Rahul Sharma

Enter Age : 45

Enter Mobile : 9876543210

Enter Specialization : Cardiologist

Enter Experience : 18

Enter Consultation Fee : 1500

Sample Output

Doctor Added Successfully



----------- Doctor Details -----------



Doctor ID          : 101

Name               : Rahul Sharma

Age                : 45

Mobile             : 9876543210

Specialization     : Cardiologist

Experience         : 18 Years

Consultation Fee   : ₹1500'''



class Person:
    def __init__(self,person_id,name,age,mobile_no):
        self.id = person_id
        self.name = name
        self.age = age
        self.mobile_no = mobile_no

    def display(self):
        pass

class Doctor(Person):
    def __init__(self, person_id, name, age, mobile_no, specialization, experience, fee):
        super().__init__(person_id, name, age, mobile_no)
        self.specialization = specialization
        self.experience = experience
        self.fee = fee

    def display(self):
        print("\n----------- Doctor Details -----------")
        print(f"Doctor ID          : {self.id}")
        print(f"Name               : {self.name}")
        print(f"Age                : {self.age}")
        print(f"Mobile             : {self.mobile_no}")
        print(f"Specialization     : {self.specialization}")
        print(f"Experience         : {self.experience} Years")
        print(f"Consultation Fee   : ₹{self.fee}")

class Nurse(Person):
    def __init__(self, person_id, name, age, mobile_no, department, shift, salary):
        super().__init__(person_id, name, age, mobile_no)
        self.department = department
        self.shift = shift
        self.salary = salary

    def display(self):
        print("\n----------- Nurse Details -----------")
        print(f"Nurse ID           : {self.id}")
        print(f"Name               : {self.name}")
        print(f"Age                : {self.age}")
        print(f"Mobile             : {self.mobile_no}")
        print(f"Department         : {self.department}")
        print(f"Shift              : {self.shift}")
        print(f"Salary             : ₹{self.salary}")

class Patient(Person):
    def __init__(self, person_id, name, age, mobile_no, disease, ward_no, bill_amount):
        super().__init__(person_id, name, age, mobile_no)
        self.disease = disease
        self.ward_no = ward_no
        self.bill_amount = bill_amount

    def display(self):
        print("\n----------- Patient Details -----------")
        print(f"Patient ID         : {self.id}")
        print(f"Name               : {self.name}")
        print(f"Age                : {self.age}")
        print(f"Mobile             : {self.mobile_no}")
        print(f"Disease            : {self.disease}")
        print(f"Ward Number        : {self.ward_no}")
        print(f"Bill Amount        : ₹{self.bill_amount}")

doctors = []
nurses = []
patients = []

while True:
    print("\n========== Hospital Management ==========")
    print("1. Add Doctor")
    print("2. Add Nurse")
    print("3. Add Patient")
    print("4. Display Doctor Details")
    print("5. Display Nurse Details")
    print("6. Display Patient Details")
    print("7. Exit")
    
    choice = input("Enter Choice : ")
    
    if choice == '1':
        d_id = input("\nEnter Doctor ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        mobile = input("Enter Mobile : ")
        spec = input("Enter Specialization : ")
        exp = input("Enter Experience : ")
        fee = input("Enter Consultation Fee : ")
        doc = Doctor(d_id, name, age, mobile, spec, exp, fee)
        doctors.append(doc)
        print("Doctor Added Successfully")
        
    elif choice == '2':
        n_id = input("\nEnter Nurse ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        mobile = input("Enter Mobile : ")
        dept = input("Enter Department : ")
        shift = input("Enter Shift (Day/Night) : ")
        salary = input("Enter Salary : ")
        nur = Nurse(n_id, name, age, mobile, dept, shift, salary)
        nurses.append(nur)
        print("Nurse Added Successfully")
        
    elif choice == '3':
        p_id = input("\nEnter Patient ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        mobile = input("Enter Mobile : ")
        dis = input("Enter Disease : ")
        ward = input("Enter Ward Number : ")
        bill = input("Enter Bill Amount : ")
        pat = Patient(p_id, name, age, mobile, dis, ward, bill)
        patients.append(pat)
        print("Patient Added Successfully")
        
    elif choice == '4':
        for d in doctors:
            d.display()
            
    elif choice == '5':
        for n in nurses:
            n.display()
            
    elif choice == '6':
        for p in patients:
            p.display()
            
    elif choice == '7':
        break