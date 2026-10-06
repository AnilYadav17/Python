'''8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5'''


num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1:
            print(j,end="")
        elif j==1:
            print(i,end="")
        elif i==num or j==num:
            print(num,end="")
        else:
            print(" ",end="")
    print()