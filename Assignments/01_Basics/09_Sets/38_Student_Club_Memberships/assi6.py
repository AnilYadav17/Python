'''6.
=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}'''

s1 = ""
s2 = ""
common=set()

while True:
  print("""\n=========================================
COMMON CHARACTER FINDER
=========================================
Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit""")
  c = int(input("Enter choice: "))

  match c:
    case 1:
      s1 = input("\nEnter first string: ")

    case 2:
      s2 = input("\nEnter second string: ")

    case 3:
      s1=set(s1)
      s2=set(s2)
      for i in s1.intersection(s2):
        print(i,end=" ")

    case 4:
      s1=set(s1)
      s2=set(s2)
      print(f"\nTotal common characters are {len(s1.intersection(s2))}")
    case 5:
      print("\nThanks for visiting COMMON CHARACTER FINDER ")
      break

    case _:
      print("Invalid choice")
