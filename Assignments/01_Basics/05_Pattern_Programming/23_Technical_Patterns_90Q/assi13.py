'''13.
1
01
101
0101
10101'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()