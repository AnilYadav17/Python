'''44.
    1
   22
  333
 4444
55555'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for space in range(num-1,i-1,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end="")
    print()