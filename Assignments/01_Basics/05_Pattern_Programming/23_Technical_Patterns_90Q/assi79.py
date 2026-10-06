'''79.
1
12
1 3
1  4
1 3
12
1
'''

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    #upper half
    for j in range(1,i+1):
        if j==1 or j==i:
            print(j,end="")
        else:
            print(" ",end="")
for i in range(num-1,0,-1):
    print()
    #lower half
    for j in range(1,i+1):
        if j==1 or j==i:
            print(j,end="")
        else:
            print(" ",end="")