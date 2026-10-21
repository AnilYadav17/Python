'''5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.'''

isbn_set = set()

while True:
  print("""\n=========================================
LIBRARY ISBN MANAGER
=========================================
Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit""")
  c = int(input("Enter choice: "))

  match c:
    case 1:
      n = int(input("Enter number of ISBNs to add: "))
      for i in range(n):
        isbn_set.add(input(f"Enter {i+1} ISBN: "))
      
    case 2:
      t = input("Enter ISBN to remove: ")
      if t in isbn_set:
        isbn_set.remove(t)
        print(f"Successfully removed {t}")
      else:
        print(f"{t} not found in ISBN list")
    
    case 3:
      t = input("Enter ISBN to search: ")
      if t in isbn_set:
        print("ISBN exists")
      else:
        print("ISBN not found")
    
    case 4:
      for i in isbn_set:
        print(i, end=" ")
      print()
      
    case 5:
      print(f"Total unique books are {len(isbn_set)}")

    case 6:
      print("Thanks for visiting LIBRARY ISBN MANAGER ")
      break

    case _:
      print("Invalid choice")
