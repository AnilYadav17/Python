'''1) Hollow Pyramid
    *
   * *
  *   *
 *     *
*********
'''

num = int(input("Enter Number: "))
i = 1
while i<=num:
    print()
    j=1
    while j<num*2-1:
        if i==num or i+j==num+1 or j-i==num-1:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
