'''37.
*****
####
***
##
*
'''

num = int(input("Enter Number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
    print()