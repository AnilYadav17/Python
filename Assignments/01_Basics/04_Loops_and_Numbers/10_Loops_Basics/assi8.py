# 8. Count Odd Digits
num = int(input("Number = "))
count = 0
while num > 0:
    if (num % 10) % 2 != 0:
        count += 1
    num //= 10
print("Odd digits count =", count)
