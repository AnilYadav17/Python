ch = input("Enter Consonent or Vowel ").lower()
 
match ch:
    case "a"|"e"|"i"|"o"|"u":   #can not use "or" 
        print("Vowels")
    case "$"|"&":
        print("Special Characters ")
    case _:
        print("Consonent")