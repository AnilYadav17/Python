from patient import add_patient, display_patients, search_patient
from doctor import add_doctor, display_doctors
from appointment import book_appointment, show_appointments
from billing import generate_bill


while True:
        print("\n========== Hospital Management System ==========")
        print("1. Add Patient")
        print("2. Display Patients")
        print("3. Search Patient")
        print("4. Add Doctor")
        print("5. Display Doctors")
        print("6. Book Appointment")
        print("7. Show Appointments")
        print("8. Generate Bill")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_patient()
        elif choice == '2':
            display_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            add_doctor()
        elif choice == '5':
            display_doctors()
        elif choice == '6':
            book_appointment()
        elif choice == '7':
            show_appointments()
        elif choice == '8':
            generate_bill()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

