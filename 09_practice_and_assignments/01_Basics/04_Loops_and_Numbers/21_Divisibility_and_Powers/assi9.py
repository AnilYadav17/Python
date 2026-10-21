num = int(input("Enter Number = "))
i = 1

while i <= num:
    

    space = num - 1
    while space >= i:
        print(" ", end="")
        space -= 1

    j = 1
    while j <= i:
        if j % 2 != 0:
            print("1", end="")
        else:
            print("0", end="")
        j += 1

    print()
    i += 1