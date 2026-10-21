'''24.
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *'''

num = int(input("Enter Number: "))

for i in range(1,num+1):
    for numbers in range(1,num+1):
        if i ==numbers or i+numbers==num+1:
            print("*",end="")
        else:
            print(" ",end="")
    
    print()
