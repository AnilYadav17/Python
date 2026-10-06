def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

while True:
    print("""
1. Addition
2. Substraction
3. Multiplication""")
    a,b = map(int,input("Enter Two Numbers: ").split())
    n  = int(input("Enter Choice: "))
    match n:
        case 1:
            sum(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case _:
            break
