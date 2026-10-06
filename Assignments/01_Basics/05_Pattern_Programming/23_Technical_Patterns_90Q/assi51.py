'''51.
 55555
  4444
   333
    22
     1'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for space in range(1,i):
        print(" ",end="")
    for j in range(1,num-i+2):
        print(num-i+1,end="")
    print()