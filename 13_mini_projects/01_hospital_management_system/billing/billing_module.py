def generate_bill():
    p_Id = input("Enter Patient ID: ")
    try:
        c_Charges = float(input("Enter Consultation Charges: "))
        m_Cost = float(input("Enter Medicine Cost: "))
        t_Charges = float(input("Enter Test Charges: "))
    except ValueError:
        print("Invalid input for charges. Please enter numeric values.")
        return
        
    total_bill = c_Charges + m_Cost + t_Charges
    print("\n--- Bill Details ---")
    print(f"Patient ID: {p_Id}")
    print(f"Consultation Charges: {c_Charges}")
    print(f"Medicine Cost: {m_Cost}")
    print(f"Test Charges: {t_Charges}")
    print(f"Total Bill: {total_bill}")
    print("--------------------\n")
