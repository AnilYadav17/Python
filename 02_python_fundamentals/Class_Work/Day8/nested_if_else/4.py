username = input("Enter Username:")
password = input("Enter Password:")

if username=="admin":
    if password=="1234":
        print("Logged in")
    else:
        print("Password Invalid!")
else:
    print("Invalid Username!")
