students = {}
while True:
    print("=========================================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("=========================================")
    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit")

    c = int(input("Enter your choice: "))
    match c:
        case 1:
            n = int(input("How many students to add: "))
            for i in range(n):
                sid = input("\nEnter Student ID: ")
                if sid in students:
                    print("Student ID Already Exists")
                    continue
                name = input("Enter Student Name: ")
                course = input("Enter Course Name: ")
                mobile = input("Enter Mobile Number: ")
                fees = int(input("Enter Fees: "))
                city = input("Enter City: ")
                students[sid] = {
                    "name": name,
                    "course": course,
                    "mobile": mobile,
                    "fees": fees,
                    "city": city
                }
                print("Student Added Successfully")
        case 2:
            sid = input("Enter Student ID: ")
            if sid in students:
                s = students[sid]
                print(f"\nStudent ID : {sid}")
                print(f"Name       : {s['name']}")
                print(f"Course     : {s['course']}")
                print(f"Mobile     : {s['mobile']}")
                print(f"Fees       : {s['fees']}")
                print(f"City       : {s['city']}")
            else:
                print("Student Not Found")
        case 3:
            sid = input("Enter Student ID: ")
            if sid in students:
                new_course = input("Enter new course name: ")
                students[sid]["course"] = new_course
                print("Course Updated Successfully")
            else:
                print("Student Not Found")
        case 4:
            sid = input("Enter Student ID: ")
            if sid in students:
                del students[sid]
                print("Student Deleted Successfully")
            else:
                print("Student Not Found")
        case 5:
            for sid, s in students.items():
                print("-----------------------------------")
                print(f"Student ID : {sid}")
                print(f"Name       : {s['name']}")
                print(f"Course     : {s['course']}")
                print(f"Fees       : {s['fees']}")
            if students:
                print("-----------------------------------")
        case 6:
            print(f"Total Students : {len(students)}")
        case 7:
            course = input("Enter Course : ")
            found = False
            for sid, s in students.items():
                if s["course"].lower() == course.lower():
                    print(f"{sid}  {s['name']}")
                    found = True
            if not found:
                print("No Students Found")
        case 8:
            city = input("Enter City : ")
            found = False
            for sid, s in students.items():
                if s["city"].lower() == city.lower():
                    print(f"{sid}  {s['name']}")
                    found = True
            if not found:
                print("No Students Found")
        case 9:
            if students:
                highest_sid = max(students, key=lambda k: students[k]['fees'])
                s = students[highest_sid]
                print("\nHighest Fee Paying Student")
                print(f"Student ID : {highest_sid}")
                print(f"Name       : {s['name']}")
                print(f"Course     : {s['course']}")
                print(f"Fees       : {s['fees']}")
            else:
                print("No students available.")
        case 10:
            if students:
                lowest_sid = min(students, key=lambda k: students[k]['fees'])
                s = students[lowest_sid]
                print("\nLowest Fee Paying Student")
                print(f"Student ID : {lowest_sid}")
                print(f"Name       : {s['name']}")
                print(f"Course     : {s['course']}")
                print(f"Fees       : {s['fees']}")
            else:
                print("No students available.")
        case 11:
            print("Thank You For Using Student Management System")
            break
        case _:
            print("Invalid choice. Try again.")
