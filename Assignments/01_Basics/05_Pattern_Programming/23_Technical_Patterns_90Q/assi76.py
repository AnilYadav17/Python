'''76.
x
xx
xxx
xxxx
xxx
xx
x
'''

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    #upper half
    for j in range(1,i+1):
        print("x",end="")
for i in range(1,num):
    print()
    #lower half
    for j in range(num-1,i-1,-1):
        print("x",end="")