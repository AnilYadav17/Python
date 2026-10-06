age = int(input("Enter Age = "))

match age:
    case x if x<13:
        print("Child")
    case x if x<20:
        print("Teen")
    case x if x<50:
        print("Adult")
        