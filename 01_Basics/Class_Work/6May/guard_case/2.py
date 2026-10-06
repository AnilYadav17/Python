n = int(input("Enter Number = "))

match n:
    case x if x%2==0:
        print("Even")
    case x:
        print("Odd")
        