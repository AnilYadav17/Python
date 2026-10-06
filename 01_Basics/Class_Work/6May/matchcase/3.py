a = int(input("Enter Choice = "))
match a%2:
    case 0:
        print("even")
    case 1:
        print("Odd")
    case _:
        print("Wrong")