'''49.
    1
   10
  101
 1010
10101'''


num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        if k%2!=0:
            print("1",end="")
        else:
            print("0",end="")
    print()