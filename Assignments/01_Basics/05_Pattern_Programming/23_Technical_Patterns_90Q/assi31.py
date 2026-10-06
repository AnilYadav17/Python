'''31.
12345
1234
123
12
1
'''

num = int(input("Enter Number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()