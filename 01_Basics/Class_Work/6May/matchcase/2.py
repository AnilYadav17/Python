a = int(input("Enter Choice = "))
match a:
    case 0:
        print("Threee")
    case 1:
        print("One")
    case 2|3|4:
        print("Two or Three or Four")
    case _:
        print("Wrong")