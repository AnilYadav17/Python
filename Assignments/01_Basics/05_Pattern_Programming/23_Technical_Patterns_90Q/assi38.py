'''38.
55555
4  4
3 3
22
1

'''

num = int(input("Enter Number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        if j==1 or i==num or j==i:
            print(i,end="")
        else:
            print(" ",end="")
    print()