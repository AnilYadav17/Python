'''53.
55555
 4__4
  3_3
   22
    1'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for space in range(1,i):
        print(" ",end="")
    for j in range(1,num-i+2):
        if i==1 or j==1 or j==num-i+1: 
            print(num-i+1,end="")
        else:
            print("_",end="")
    print()