'''59.
    A
   A B
  A B C
 A B C D
A B C D E'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # spaces
    for space in range(num - i):
        print(" ", end="")

    # star
    for star in range(1,i*2):
        if star%2!=0:
            print(chr(star//2+65),end="")
        else:
            print(" ",end="")
    print()
