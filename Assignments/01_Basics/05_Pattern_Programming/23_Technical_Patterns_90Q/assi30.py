'''30.
*****
****
***
**
*
'''
num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(num,i-1,-1):
        print("*",end="")
    print()