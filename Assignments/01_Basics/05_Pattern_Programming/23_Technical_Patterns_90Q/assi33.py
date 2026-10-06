'''33.
ABCDE
ABCD
ABC
AB
A'''

num = int(input("Enter Number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(chr(ord("A")+j-1),end="")
    print()