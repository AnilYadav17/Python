'''19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5'''


num = int(input("Enter Number: "))
for i in range(1,num+1):
    print()
    for j in range(1,num+1):
        if i==1 and j==1 or i==1 and  j==num  or j==1 and i==num or j==num and i==num:
            print(num,end="")
        else:
            print(" ",end="") 