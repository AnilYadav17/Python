patients = {}

def add_patient():
    p_Id = input("Enter Patient ID: ")
    p_Name = input("Enter Patient Name: ")
    p_Age = input("Enter Patient Age: ")
    p_Gender = input("Enter Patient Gender: ")
    p_Disease = input("Enter Disease: ")
    p_Mobile = input("Enter Mobile Number: ")
    patients[p_Id] = {
        "Name": p_Name,
        "Age": p_Age,
        "Gender": p_Gender,
        "Disease": p_Disease,
        "Mobile": p_Mobile
    }
    print("Patient added successfully!")

def display_patients():
    if not patients:
        print("No patients registered.")
        return
    for pid, details in patients.items():
        print(f"ID: {pid}, Name: {details['Name']}, Age: {details['Age']}, Gender: {details['Gender']}, Disease: {details['Disease']}, Mobile: {details['Mobile']}")

def search_patient():
    p_Id = input("Enter Patient ID to search: ")
    if p_Id in patients:
        details = patients[p_Id]
        print("Patient Found:")
        print(f"ID: {p_Id}, Name: {details['Name']}, Age: {details['Age']}, Gender: {details['Gender']}, Disease: {details['Disease']}, Mobile: {details['Mobile']}")
    else:
        print("Patient not found.")
