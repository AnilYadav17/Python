# 10. Even Numbers Between Two Numbers
a = int(input("Start = "))
b = int(input("End = "))
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=" ")
