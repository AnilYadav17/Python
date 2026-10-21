'''2) Hollow Rectangle
    *********
    *       *
    *       *
    *       *
    *********'''

num = int(input("Enter Numbe: "))
i=1
while i<=num:
    print()
    j=1
    while j<num*2:
        if i==1 or i==num or j==1 or j==num*2-1:
            print("*", end="")
        else:
            print(" ",end="")
        j+=1
    i+=1