'''48.
    A
   AB
  A_C
 A__D
ABCDE
'''



num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        if i==num or k==1 or k==i:
            print(chr(ord("A")+k-1),end="")
        else:
            print("_",end="")
    print()