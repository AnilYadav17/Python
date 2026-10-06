'''1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.'''

coding_club=set()
robotics_club=set()

while True:
  print("""\n
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================
Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit""")
    
  choice = int(input("Enter choice: "))
  match choice:
    case 1:
      n = int(input("Enter Number of Students: "))
      for i in range(n):
        coding_club.add(input(f"Enter ID of student{i+1}: "))

    case 2:
      n = int(input("Enter Number of Students: "))
      for i in range(n):
        robotics_club.add(input(f"Enter ID of student{i+1}: "))
        
    case 3:
      print("\nStudents in Coding Club: ")
      for i in coding_club:
        print(i,end=" ")

    case 4:
      print("\nStudents in Robotics Club: ")
      for i in robotics_club:
        print(i,end=" ")

    case 5:
      print("\nStudents in Both Clubs: ")
      for i in coding_club.intersection(robotics_club):
        print(i,end=" ")

    case 6:
      print("\nStudents only in Coding Club: ")
      for i in coding_club.difference(robotics_club):
        print(i,end=" ")
    
    case 7:
      print("\nStudents only in Robotics Club: ")
      for i in robotics_club.difference(coding_club):
        print(i,end=" ")

    case 8:
      print("\nUnique Students in both Clubs: ")
      for i in robotics_club.union(coding_club):
        print(i,end=" ")

    case 9:
      print(f"\nTotal Unique Club Members: {len(robotics_club.union(coding_club))}")

    case 10:
      print("/n Thank you for visiting...")
      break