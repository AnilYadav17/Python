'''3) X Star Pattern
    *   *
     * *
      *
     * *
    *   *'''

num = int(input("Enter Number:"))
i = 1
while i<=num:
    print()
    j=1
    while j<=num:
        if i==j or i+j==num+1:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    i+=1