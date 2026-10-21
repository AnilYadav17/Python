n1, n2 = map(int, input("Enter two numbers = ").split())
count = 0

if n1 < n2:
    for i in range(n1, n2 + 1):
        if i % 7 == 0:
            count += 1
    print("Count =", count)

elif n1 > n2:
    for i in range(n1, n2 - 1, -1):
        if i % 7 == 0:
            count += 1
    print("Count =", count)

else:
    if n1 % 7 == 0:
        print("Same Number and Divisible by 7")
    else:
        print("Same number and Not Divisible by 7")
