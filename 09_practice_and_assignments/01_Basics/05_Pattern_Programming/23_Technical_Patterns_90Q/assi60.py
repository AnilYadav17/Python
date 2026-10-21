'''60.
    X
   X X
  X__X
 X____X
X X X X X'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # spaces
    for space in range(num - i):
        print(" ", end="")

    # star
    for star in range(1,i*2):
        if star==1 or star==i*2-1 :
            print("X",end="")
        elif i == num:
            if star % 2 != 0:
                print("X", end="")
            else:
                print(" ", end="")
        else:
            print("_",end="")
    print()