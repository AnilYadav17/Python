'''54.
ABCDE
 A__D
  A_C
   AB
    A'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for space in range(1,i):
        print(" ",end="")
    for j in range(1,num-i+2):
        if i==1 or j==1 or j==num-i+1: 
            print(chr(ord("A")+j-1),end="")
        else:
            print("_",end="")
    print()
