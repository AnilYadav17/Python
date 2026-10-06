'''55.
ABCDE
 ABCD
  ABC
   AB
    A
'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for space in range(1,i):
        print(" ",end="")
    for j in range(1,num-i+2):
            print(chr(ord("A")+j-1),end="")
    print()
