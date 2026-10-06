'''23) Plus Star Pattern
        *
        *
    *********
        *
        *'''
    
num = int(input("Enter Number: "))

for i in range(1,num*2):
    for star in range(1,num*2):
        if star==num or i==num:
            print("*",end="")
        else:
            print(" ",end="")
    print()