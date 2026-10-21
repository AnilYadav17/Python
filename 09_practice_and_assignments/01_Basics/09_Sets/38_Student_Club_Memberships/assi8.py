'''8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.'''

allowed = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
username = ""

while True:
  print("""\n=========================================
ALLOWED CHARACTER VALIDATOR
=========================================
Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit""")
  c = int(input("Enter choice: "))

  match c:
    case 1:
      username = input("\nEnter Username: ")

    case 2:
      if username == "":
        print("\nNo username entered yet. Please enter username first.")
      else:
        if set(username).issubset(allowed):
          print("\nUsername is Valid.")
        else:
          print("\nUsername is Invalid.")

    case 3:
      print("\nAllowed Characters: ")
      for i in sorted(allowed):
        print(i, end=" ")
      print()

    case 4:
      print("\nThanks for visiting ALLOWED CHARACTER VALIDATOR ")
      break

    case _:
      print("Invalid choice")
