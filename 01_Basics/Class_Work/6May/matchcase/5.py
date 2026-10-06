a =int(input("Enter Number1 = "))
b =int(input("Enter Number2 = "))
op = input("Enter Operator = ")
match op:
    case "+":
        print("Result is ",(a+b))
    case "-":
        print("Result is ",(a-b))
    case "*":
        print("Result is ",(a*b))
    case "/":
        if b!=0:
            print("Result is ",(a/b))
        else:
            print("Avoid Zero")