'''20.
1
12
1 3
1  4
12345'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if j==1:
            print("1",end="")
        elif i==num:
            print(j,end="")
        elif j==i:
            print(i,end="")
        else:
            print(" ",end="")
    print()