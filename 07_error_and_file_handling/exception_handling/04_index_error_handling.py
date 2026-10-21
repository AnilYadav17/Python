try:
    l = [1,2,3,4]
    x = int(input("Enter index to access (max:4): "))
    print(l[x])

except IndexError:
    print("Please check the index")


    