'''65.
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # spaces
    for space in range(num - i):
        print(" ", end="")

    value = 1

    for j in range(1, i + 1):

        print(value, end=" ")

        value = value * (i - j) // j

    print()