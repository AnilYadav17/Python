'''=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
'''


from collections import namedtuple
Patient = namedtuple("Patients",["patient_id","patient_name","age","disease"])
N = int(input("Enter Number of Patients: "))

patient=[]
for i in range(N):
    print(f"Enter patient{i+1} Details: ")
    id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")
    patient.append(Patient(id,name,age,disease))


print("\n All Patient Details: ")
for i in range(N):
    print(*patient[i])
print()

p_id = input("\nEnter Patient Id: ")
p_disease = input("Enter Disease: ")


x=-1
print(f"Checking.. if Patient found with {p_id} and {p_disease}: ")
for i in range(len(patient)):
    if patient[i].patient_id==p_id and patient[i].disease==p_disease:
        print("Patient Found: ")
        print("\n",*patient[i])
    else:
        print("Patient not found ")

    
print("\n Patients Above 60: ")
for i in range(len(patient)):
    if patient[i].age>60:
        print("\n",*patient[i])

count=0
print("\n Patients with Diabetes: ")
for i in range(len(patient)):
    if patient[i].disease=="Diabetes":
       count+=1
print("",count)