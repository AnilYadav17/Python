patients = {}
while True:
    print("=====================================")
    print(" HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("=====================================")
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")
    
    c = int(input("Enter your choice: "))
    match c:
        case 1:
            n = int(input("How many patients to add: "))
            for i in range(n):
                pid = input("\nEnter Patient ID: ")
                if pid in patients:
                    print("Patient ID already exists.")
                    continue
                name = input("Enter Patient Name: ")
                age = int(input("Enter Age: "))
                gender = input("Enter Gender: ")
                disease = input("Enter Disease: ")
                doctor = input("Enter Doctor Name: ")
                patients[pid] = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "disease": disease,
                    "doctor": doctor
                }
                print("Patients Added Successfully.")
        case 2:
            pid = input("Enter Patient ID: ")
            if pid in patients:
                p = patients[pid]
                print(f"\nPatient ID : {pid}")
                print(f"Name       : {p['name']}")
                print(f"Age        : {p['age']}")
                print(f"Gender     : {p['gender']}")
                print(f"Disease    : {p['disease']}")
                print(f"Doctor     : {p['doctor']}")
            else:
                print("Patient Record Not Found")
        case 3:
            pid = input("Enter Patient ID: ")
            if pid in patients:
                new_disease = input("Enter new disease: ")
                patients[pid]["disease"] = new_disease
                print("Disease Updated Successfully")
            else:
                print("Patient Record Not Found")
        case 4:
            pid = input("Enter Patient ID: ")
            if pid in patients:
                del patients[pid]
                print("Patient Record Deleted Successfully")
            else:
                print("Patient Not Found")
        case 5:
            for pid, p in patients.items():
                print("--------------------------------")
                print(f"Patient ID : {pid}")
                print(f"Name       : {p['name']}")
                print(f"Age        : {p['age']}")
                print(f"Disease    : {p['disease']}")
                print(f"Doctor     : {p['doctor']}")
            if patients:
                print("--------------------------------")
        case 6:
            print(f"Total Patients : {len(patients)}")
        case 7:
            disease = input("Enter Disease : ")
            found = False
            for pid, p in patients.items():
                if p["disease"].lower() == disease.lower():
                    print(f"{pid}  {p['name']}")
                    found = True
            if not found:
                print("No Patient Found")
        case 8:
            if patients:
                oldest_pid = max(patients, key=lambda k: patients[k]['age'])
                p = patients[oldest_pid]
                print("\nOldest Patient Details")
                print(f"Patient ID : {oldest_pid}")
                print(f"Name       : {p['name']}")
                print(f"Age        : {p['age']}")
                print(f"Disease    : {p['disease']}")
                print(f"Doctor     : {p['doctor']}")
            else:
                print("No patients available.")
        case 9:
            if patients:
                youngest_pid = min(patients, key=lambda k: patients[k]['age'])
                p = patients[youngest_pid]
                print("\nYoungest Patient Details")
                print(f"Patient ID : {youngest_pid}")
                print(f"Name       : {p['name']}")
                print(f"Age        : {p['age']}")
                print(f"Disease    : {p['disease']}")
                print(f"Doctor     : {p['doctor']}")
            else:
                print("No patients available.")
        case 10:
            print("Thank You For Using Hospital Patient Management System")
            break
        case _:
            print("Invalid choice. Please try again.")
