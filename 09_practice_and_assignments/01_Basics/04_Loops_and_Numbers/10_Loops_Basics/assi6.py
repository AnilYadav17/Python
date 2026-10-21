# 6. Armstrong
num = int(input("Number = "))
temp = num
total = 0
while num > 0:
    digit = num % 10
    total += digit**3
    num //= 10
if total == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
