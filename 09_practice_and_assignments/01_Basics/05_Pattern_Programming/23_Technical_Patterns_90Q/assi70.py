'''70.
* * * * * 
 * * * * 
  * * * 
   * * 
    *'''


num = int(input("Enter Number: "))
for i in range(1,num+1):

    #spaces
    for spaces in range(1,i):
        print(" ",end="")
    

    #star
    for star in range(num-i+1):
        print("*",end=" ")
    print()