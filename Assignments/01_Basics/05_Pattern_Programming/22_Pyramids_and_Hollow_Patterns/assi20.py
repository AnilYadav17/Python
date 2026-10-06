'''20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1'''

'''
20) Continuous Diamond Numbers
      1
     2 3
    4 5 6
   7 8 9 10
    4 5 6
     2 3
      1
'''

num = int(input("Enter Number: "))
start = 1

# upper half
for i in range(1, num + 1):

    # spaces
    for s in range(num - i):
        print(" ", end="")

    temp = start

    # numbers
    for j in range(i):
        print(temp, end=" ")
        temp += 1

    print()

    start += i


# lower half
start = start - num - (num - 1)

for i in range(num - 1, 0, -1):

    # spaces
    for s in range(num - i):
        print(" ", end="")

    temp = start

    # numbers
    for j in range(i):
        print(temp, end=" ")
        temp += 1

    print()

    start -= (i - 1)