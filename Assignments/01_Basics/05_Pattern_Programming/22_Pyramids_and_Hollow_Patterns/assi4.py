'''4) Vertical Diamond
       *
      * *
     *   *
    *     *
     *   *
      * *
       *'''


n=int(input("Enter Number:"))
i=1
while i<n*2:
    print()
    j=1
    while j<n*2:
        if i+j==n+1 or j-i==n-1 or i-j==n-1 or i+j-n==n*2-1:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1