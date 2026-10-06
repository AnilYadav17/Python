'''
30) Extended Slanted Star Block
    ****
     ****
      ****
       ****
        ****'''

num = int(input("Enter Number: "))
count=1

for i in range(1,num+1):
    #for spaces
    for spaces in range(1,i):
        print(" ",end="")

    #for numbers
    for numbers in range(1,num):
        print("*",end="")
    print()