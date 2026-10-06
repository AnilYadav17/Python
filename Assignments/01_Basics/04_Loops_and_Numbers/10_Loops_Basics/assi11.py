# 11. Count Digit Occurrence
num = int(input("Number = "))
digit = int(input("Digit = "))
count = 0
while num > 0:
    if num % 10 == digit:
        count += 1
    num //= 10
print(count)
