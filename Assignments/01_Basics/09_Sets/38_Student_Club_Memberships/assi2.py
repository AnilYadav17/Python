'''2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.'''

python_students=set()
java_students=set()

while True:
    print("""\n=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================
Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit
""")
    choice = int(input("Enter Choice: "))
    match choice:
        case 1:
            n = int(input("Enter number of Students: "))
            for i in range(n):
                python_students.add(input(f"Enter name of Student{i+1}: "))

        case 2:
            n = int(input("Enter number of Students: "))
            for i in range(n):
                java_students.add(input(f"Enter name of Student{i+1}: "))
        
        case 3:
            print("\nPython Students: ")
            for i in python_students:
                print(i,end=" ")
        
        case 4:
            print("\nJava Students: ")
            for i in java_students:
                print(i,end=" ")
            
        case 5:
            print("\nStudents enrolled in both courses: ")
            for i in  python_students.intersection(java_students):
                print(i,end=" ")
            
        case 6:
            print("\nStudents enrolled in only Python: ")
            for i in  python_students.difference(java_students):
                print(i,end=" ")
              
        case 7:
            print("\nStudents enrolled in only Java: ")
            for i in  java_students.difference(python_students):
                print(i,end=" ")

        case 8:
            i = input("\nStudents name to check Enrollment: ")
            if i in python_students:
              print("Student Enrolled")
            else:
              print("Student Not Enrolled")
        
        case 9:
            print(f"\nTotal unique students are : {len(python_students.union(java_students))}")
        
        case 10:
            print("Thanks for visiting ONLINE COURSE MANAGEMENT SYSTEM")
            break
        
        case _:
          print("Invalid choice")