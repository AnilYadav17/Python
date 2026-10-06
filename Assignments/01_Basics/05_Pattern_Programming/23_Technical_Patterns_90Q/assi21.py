'''21.
1
22
3 3
4  4
55555
'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if j==1:
            print(i,end="")
        elif i==num:
            print(i,end="")
        elif j==i:
            print(i,end="")
        else:
            print(" ",end="")
    print()