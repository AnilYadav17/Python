n = int(input("Enter number = "))
for i in range(1,11):
    if i==5:
        pass
    elif i==9:
        break
    elif i%2==0:
        continue
    else:
        print(i)