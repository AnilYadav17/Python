# 14. Elevator System
a = int(input("Current Floor = "))
b = int(input("Destination Floor = "))
if a < b:
    for i in range(a, b+1):
        print(i, end=" → ")
elif a > b:
    for i in range(a, b-1, -1):
        print(i, end=" → ")
else:
    print("Already on same floor")
