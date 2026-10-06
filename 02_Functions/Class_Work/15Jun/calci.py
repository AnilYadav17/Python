def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)




def main():
    while True:
        print("""
1. Addition
2. Substraction
3. Multiplication""")
        n  = int(input("Enter Choice: "))
        match n:
            case 1:
                a,b = map(int,input("Enter Two Numbers: ").split())
                sum(a,b)
            case 2:
                a,b = map(int,input("Enter Two Numbers: ").split())
                sub(a,b)
            case 3:
                a,b = map(int,input("Enter Two Numbers: ").split())
                mul(a,b)
            case _:
                break

main()