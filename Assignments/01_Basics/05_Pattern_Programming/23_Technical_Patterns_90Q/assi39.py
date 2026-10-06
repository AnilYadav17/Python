'''39.
123456
54321
1234
321
12
1'''

'''39.
123456
54321
1234
321
12
1
'''

num = int(input("Enter Number: "))

for i in range(num, 0, -1):
    if i % 2 == 0:
        for j in range(1, i + 1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    print()