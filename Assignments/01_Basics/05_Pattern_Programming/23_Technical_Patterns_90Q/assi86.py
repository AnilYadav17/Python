'''86.
**********
****  ****
***    ***
**      **
*        *'''


num = int(input("Enter Number: "))
for i in range(1,num+2):
    
    #left stars
    for stars in range(num-i+1):
        print("*",end="")
    
    #space
    for space in range(1,(i)*2-1):
        print(" ",end="")

    #right stars
    for stars in range(num-i+1):
        print("*",end="")
    print()