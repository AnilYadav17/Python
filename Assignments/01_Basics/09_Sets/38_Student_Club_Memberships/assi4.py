'''4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.'''


s = frozenset({"Python","Java","MySQL","React","Spring Boot"})

while True:
  print("""\n=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================
Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit
""")
  c = int(input("Enter choice: "))
  match c:
    case 1:
      for i in s:
        print(i,end=" ")
      print()

    case 2:
      search = input("\nEnter subject to search: ")
      if search in s:
        print("\nSubject exists")
      else:
        print("\nSubject not exist")

    case 3:
      print(f"\nTotal Subjects {len(s)}")

    case 4:
      a = input("Enter Subject: ")
      s.add(a)
    
    case 5:
      print("Thanks for visiting FROZEN SET SUBJECT MANAGEMENT...")
      break

    case _:
      print("Invalid choice")