num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # Print dashes
    for j in range(num - i):
        print("-", end=" ")

    # Print numbers
    for k in range(i):
        print(i + k, end=" ")

    print()