'''7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.'''

s = set("abcdefghijklmnopqrstuvwxyz")
sentence = ""

while True:
  print("""\n=========================================
MISSING ALPHABET FINDER
=========================================
Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit""")
  c = int(input("Enter choice: "))

  match c:
    case 1:
      sentence = input("\nEnter sentence: ")

    case 2:
      missing = s.difference(set(sentence.lower()))
      print("\nMissing alphabets: ")
      for i in sorted(missing):
        print(i, end=" ")
      print()

    case 3:
      missing = s.difference(set(sentence.lower()))
      print(f"\nTotal missing alphabets: {len(missing)}")

    case 4:
      print("\nThanks for visiting MISSING ALPHABET FINDER ")
      break

    case _:
      print("Invalid choice")
