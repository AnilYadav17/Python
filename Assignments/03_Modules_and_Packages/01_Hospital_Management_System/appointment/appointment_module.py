appointments = []

def book_appointment():
    a_Id = input("Enter Appointment ID: ")
    p_Id = input("Enter Patient ID: ")
    d_Id = input("Enter Doctor ID: ")
    a_Date = input("Enter Appointment Date: ")
    a_Time = input("Enter Appointment Time: ")
    
    appointments.append({
        "Appointment ID": a_Id,
        "Patient ID": p_Id,
        "Doctor ID": d_Id,
        "Date": a_Date,
        "Time": a_Time
    })
    print("Appointment booked successfully!")

def show_appointments():
    if not appointments:
        print("No appointments booked.")
        return
    for app in appointments:
        print(f"Appointment ID: {app['Appointment ID']}, Patient ID: {app['Patient ID']}, Doctor ID: {app['Doctor ID']}, Date: {app['Date']}, Time: {app['Time']}")
