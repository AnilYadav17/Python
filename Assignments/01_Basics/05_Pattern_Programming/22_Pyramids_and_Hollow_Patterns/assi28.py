'''28) Hollow Square
    *****
    *   *
    *   *
    *   *
    *****'''

num = int(input("Enter Number: "))
count=1

for i in range(1,num+1):
    #for numbers
    for numbers in range(1,num+1):
        if i==1 or i==num or numbers==1 or numbers==num:
            print("*",end="")
        else:
            print(" ",end="")
    print()