# 7. Count Even Digits
num = int(input("Number = "))
count = 0
while num > 0:
    if (num % 10) % 2 == 0:
        count += 1
    num //= 10
print("Even digits count =", count)
