'''27.
1
10
1 1
1  0
10101'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):
    for j in range(1, i + 1):

        if j==1 :
            print("1",end="")
        elif i==num and j%2!=0:
            print("1",end="")
        elif i==num and j%2==0:
            print("0",end="")
        elif i==j and j%2==0:
            print("0",end="")
        elif i==j and j%2!=0:
            print("1",end="")
        else:
            print(" ", end="")

    print()