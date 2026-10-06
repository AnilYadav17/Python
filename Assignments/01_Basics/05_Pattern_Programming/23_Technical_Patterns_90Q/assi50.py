'''50.
12345
 1234
  123
   12
    1'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for space in range(1,i):
        print(" ",end="")
    for j in range(1,num-i+2):
        print(j,end="")
    print()