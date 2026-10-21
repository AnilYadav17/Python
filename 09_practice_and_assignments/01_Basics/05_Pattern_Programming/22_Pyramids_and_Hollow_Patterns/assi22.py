'''
22) Inverted Hollow Pyramid
*********
 *     *
  *   *
   * *
    *
'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # for spaces
    for spaces in range(1, i):
        print(" ", end="")

    # for star
    for star in range((num - i) * 2 + 1, 0, -1):

        if i == 1 or i == num or star == 1 or star == (num - i) * 2 + 1:
            print("*", end="")

        else:
            print(" ", end="")

    print()