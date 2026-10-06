'''46.
    A
   AB
  ABC
 ABCD
ABCDE'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for k in range(num+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(ord("A")+j-1),end="")
    print()