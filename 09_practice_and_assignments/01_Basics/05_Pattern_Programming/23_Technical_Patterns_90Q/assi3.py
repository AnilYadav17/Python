'''3.
*
 *
  *
   *
    *'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()