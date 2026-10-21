# 12. Product of Digits
num = int(input("Number = "))
prod = 1
while num > 0:
    prod *= num % 10
    num //= 10
print(prod)
if prod % 2 == 0:
    print("Even")
else:
    print("Odd")
