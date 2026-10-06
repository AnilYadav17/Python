'''41.
A
BCD
EFGHI
JKLMNOP
'''

num = int(input("Enter Number: "))
c = ord("A")

for i in range(1, num + 1):

    for j in range(1, 2*i):

        print(chr(c), end="")
        c += 1

    print()