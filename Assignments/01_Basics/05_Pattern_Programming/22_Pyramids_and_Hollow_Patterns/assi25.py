'''
25) Number Sandglass
123454321
 1234321
  12321
   121
    1
   121
  12321
 1234321
123454321
'''

num = int(input("Enter Number: "))

for i in range(1, num * 2):

    # spaces
    for s in range(num - (abs(num - i) + 1)):
        print(" ", end="")

    # increasing
    for j in range(1, abs(num - i) + 2):
        print(j, end="")

    # decreasing
    for j in range(abs(num - i), 0, -1):
        print(j, end="")

    print()