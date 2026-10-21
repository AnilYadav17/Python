'''36.
ABCDE
A  D
A C
AB
A'''

num = int(input("Enter Number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        if j==1 or i==num or j==i:
            print(chr(ord("A")+j-1),end="")
        else:
            print(" ",end="")
    print()