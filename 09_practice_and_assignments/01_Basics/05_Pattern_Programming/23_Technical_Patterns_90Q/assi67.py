'''67.
    A
   B B
  C   C
 D     D
EEEEEEEEE'''



num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # spaces
    for space in range(num - i):
        print(" ", end="")

    value = 1

    for j in range(1, num*2):
        if i==num or j==1 or 2*i-1==j:
            print(chr(ord("A")+i-1),end="")
        else:
            print(" ",end="")
        if j==2*i-1==j:
            break

    print()