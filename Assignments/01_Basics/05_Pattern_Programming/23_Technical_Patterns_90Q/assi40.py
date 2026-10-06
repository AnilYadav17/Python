'''40.
*
**
****
*******
***********
'''

num = int(input("Enter Number: "))
stars = 1

for i in range(1, num + 1):
    for j in range(stars):
        print("*", end="")
    print()
    stars = stars + i