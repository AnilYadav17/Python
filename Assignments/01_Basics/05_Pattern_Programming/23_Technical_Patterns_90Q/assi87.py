'''
87.
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

num = int(input("Enter Number: "))

# upper half
for i in range(1, num + 1):

    # left stars
    for stars in range(num - i + 1):
        print("*", end="")

    # spaces
    for space in range((i - 1) * 2):
        print(" ", end="")

    # right stars
    for stars in range(num - i + 1):
        print("*", end="")

    print()

# lower half
for i in range(1, num + 1):

    # left stars
    for stars in range(i):
        print("*", end="")

    # spaces
    for space in range((num - i) * 2):
        print(" ", end="")

    # right stars
    for stars in range(i):
        print("*", end="")

    print()