# 13. Number Range Display
a = int(input("First = "))
b = int(input("Second = "))
if a < b:
    for i in range(a, b+1):
        print(i, end=" ")
elif a > b:
    for i in range(a, b-1, -1):
        print(i, end=" ")
else:
    print("Both numbers are same")
