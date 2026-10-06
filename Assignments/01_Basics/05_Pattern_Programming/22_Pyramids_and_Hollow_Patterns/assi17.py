'''17) Hollow Hourglass
      * * * * *
        *   *
         * *
          *
         * *
       *     *
      * * * * *'''

num = int(input("Enter Number: "))
for i in range(1,num*2+2):
    print()
    for j in range(1,num*2):
        if i==1 or i==num*2+1 or i-j==1 or j+i==num*2+1:
          print("*",end="")
        else:
           print(" ",end="")