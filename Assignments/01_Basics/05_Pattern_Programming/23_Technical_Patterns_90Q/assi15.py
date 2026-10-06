'''15.
A
BB
CCC
DDDD
EEEEE'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(ord("A")+i-1),end="")
    print()