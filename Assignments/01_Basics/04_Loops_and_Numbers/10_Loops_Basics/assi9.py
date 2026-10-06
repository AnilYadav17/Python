# 9. Check All Digits Even
num = int(input("Number = "))
flag = True
while num > 0:
    if (num % 10) % 2 != 0:
        flag = False
        break
    num //= 10
if flag:
    print("All Even")
else:
    print("Not All Even")
