a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = int(input("Enter d:"))

if a>b and a>c and a>d:
    print("A is Greater")
elif b>c and b>d:
    print("B is Greater")
elif c>d:
    print("C is Greater")
else:
    print("D is Greater")
