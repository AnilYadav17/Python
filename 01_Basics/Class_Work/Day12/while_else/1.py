attempts = 0
while attempts<3:
    password=input("Enter Password = ")
    if password=="admin":
        print("Logged in!")
        break
    attempts+=1
else:
    print("Attempts limit reached!")