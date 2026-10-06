'''85.
*        *
**      **
***    ***
****  ****
**********'''

num = int(input("Enter Number: "))
for i in range(1,num+2):
    
    #left stars
    for stars in range(i):
        print("*",end="")
    
    #space
    for space in range((num-i)*2+2):
        print(" ",end="")

    #right stars
    for stars in range(i):
        print("*",end="")
    print()