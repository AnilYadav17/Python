'''3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.'''

visitor=set()

while True:
  print('''\n
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================
Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit''')
  c = int(input("Enter choice: "))

  match c:
    case 1:
      n = int(input("Enter number of visitors: "))
      for i in range(n):
        visitor.add(input(f"Enter {i+1} visitor ID: "))
      
    case 2:
      t = input("Enter ID of visitor: ")
      for i in visitor:
        if i==t:
          visitor.remove(i)
          print(f"Successfully removed {t}")
          break
        else:
          print(f"{t} not found in Visitors list")
    
    case 3:
      t = input("Enter ID of visitor: ")
      if t in visitor:
        print("Valid visitor")
      else:
        print("Visitor not found")
    
    case 4:
      for i in visitor:
        print(i,end=" ")
      
    case 5:
      print(f"Total unique elements are {len(visitor)}")

    case 6:
      visitor.clear()
      print("There is no visitor left")

    case 7:
      print("Thanks for visiting VISITOR TRACKING SYSTEM ")
      break

    case _:
      print("Invalid choice")
        