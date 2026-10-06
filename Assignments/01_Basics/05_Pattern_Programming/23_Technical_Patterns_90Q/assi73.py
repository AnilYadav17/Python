'''73.
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1

'''

num = int(input("Enter Number: "))
for i in range(1,num+1):

    #spaces
    for spaces in range(1,i):
        print(" ",end="")
    #numbers
    for star in range(1,num+2-i):
            print(num-i+1,end=" ")
    print()
