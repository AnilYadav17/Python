'''45.
    5
   44
  333
 2222
11111'''

num = int(input("Enter Number: "))

for i in range(num,0,-1):
    #spaces
    for j in range(1,i):
        print(" ",end="")

    #numbers
    for k in range(num-i+1):
        print(i,end="")

    print()