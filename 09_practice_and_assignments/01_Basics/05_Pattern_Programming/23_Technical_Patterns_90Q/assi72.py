'''72.
A B C D E
 A B C D 
  A B C
   A B
    A
'''

num = int(input("Enter Number: "))
for i in range(1,num+1):

    #spaces
    for spaces in range(1,i):
        print(" ",end="")
    #numbers
    for star in range(1,num+2-i):
            print(chr(ord("A")+star-1),end=" ")
    print()
