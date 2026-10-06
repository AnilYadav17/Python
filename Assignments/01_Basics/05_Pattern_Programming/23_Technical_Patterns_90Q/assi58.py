'''58.
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # spaces
    for space in range(num - i):
        print(" ", end="")

    # star
    for star in range(1,i*2):
        if star%2!=0:
            print(star//2+1,end="")
        else:
            print(" ",end="")
    print()
