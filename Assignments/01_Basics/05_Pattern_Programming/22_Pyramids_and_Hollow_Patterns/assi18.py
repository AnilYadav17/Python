'''18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    print()
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end="")
        elif (i+j)%2!=0:
            print("0",end="")
        else:
            print(" ",end="")