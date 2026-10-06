while True:
    print("1. Say Hello!")
    print("2. Say Good Bye!")
    print("3. Exit")
    choice = int(input("Enter Choice = "))
    if choice==1:
        print("Hello!\n")
    elif choice==2:
        print("Good Bye!\n")
    else:
        print("Wrong Choice")
        break