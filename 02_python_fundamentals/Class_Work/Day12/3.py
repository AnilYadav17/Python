n = int(input("Enter number = "))
while True:
    for i in range(1,n):
        if i==5:
            pass
        elif i==9:
            break
        elif i%2==0:
            continue
        else:
            print(i)
    if i==9:
        break