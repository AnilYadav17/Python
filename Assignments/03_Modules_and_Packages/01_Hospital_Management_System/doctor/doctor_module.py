doctors = {}

def add_doctor():
    d_Id = input("Enter Doctor ID: ")
    d_Name = input("Enter Doctor Name: ")
    d_Spec = input("Enter Specialization: ")
    d_Exp = input("Enter Experience: ")
    d_Fees = float(input("Enter Consultation Fees: "))
    doctors[d_Id] = {
        "Name": d_Name,
        "Specialization": d_Spec,
        "Experience": d_Exp,
        "Fees": d_Fees
    }
    print("Doctor added successfully!")

def display_doctors():
    if not doctors:
        print("No doctors registered.")
        return
    for did, details in doctors.items():
        print(f"ID: {did}, Name: {details['Name']}, Specialization: {details['Specialization']}, Experience: {details['Experience']}, Fees: {details['Fees']}")
