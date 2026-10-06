'''
88.
    1
    2
    3
    4
123454321
    4
    3
    2
    1
'''

num = int(input("Enter Number: "))

# upper part
for i in range(1, num + 1):

    # spaces
    if i != num:
        for space in range(1, num):
            print(" ", end="")

        # number
        print(i, end="")

    else:
        # increasing
        for x in range(1, num + 1):
            print(x, end="")

        # decreasing
        for x in range(num - 1, 0, -1):
            print(x, end="")

    print()

# lower part
for i in range(num - 1, 0, -1):

    # spaces
    for space in range(1, num):
        print(" ", end="")

    # number
    print(i, end="")

    print()