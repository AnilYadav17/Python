age = int(input("Enter age:"))
citizen = input("Are you Indian(yes/no):")

if age >= 18:
    if citizen.lower()=='yes':
        print("You can Vote!")
    else:
        print("Must be Indian")
else:
    print("Age must be 18")
