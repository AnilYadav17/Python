'''29.
1
222
33333
4444444
555555555'''

num  = int(input("Enter Number:"))
for i in range(1,num+1):
    for j in range(1,i*2):
        print(i,end="")
    print()
