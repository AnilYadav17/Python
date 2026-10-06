'''
82.
\    /
 \  /
  \/
  /\
 /  \
/    \
'''

num = int(input("Enter Number: "))


#upper half
for i in range(num):

    for j in range(num * 2):

        if j == i:
            print("\\", end="")

        elif j == (num * 2 - i - 1):
            print("/", end="")

        else:
            print(" ", end="")

    print()

for i in range(num):

    for j in range(num * 2):

        if j == num - i - 1:
            print("/", end="")

        elif j == num + i:
            print("\\", end="")

        else:
            print(" ", end="")

    print()