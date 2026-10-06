'''23.
a
bc
d f
g  j
klmno'''

num = int(input("Enter Number: "))
c = ord("a")

for i in range(1, num + 1):
    for j in range(1, i + 1):

        if j == 1 or j == i or i == num:
            print(chr(c), end="")
        else:
            print(" ", end="")
        c+=1

    print()