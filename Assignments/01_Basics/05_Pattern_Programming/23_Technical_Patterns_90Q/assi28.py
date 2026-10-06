'''28.
1
123
12345
1234567
123456789'''

num  = int(input("Enter Number:"))
for i in range(1,num+1):
    for j in range(1,i*2):
        print(j,end="")
    print()
