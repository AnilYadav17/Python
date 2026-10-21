'''7.
1
00
111
0000
11111'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if i%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()