n = int(input("Enter number = "))
p = len(str(n))
sum = 0
m=n

while n>0:
    digit = n%10
    sum += digit**p
    n=n//10

if m==sum:
    print("Armstrong number ")
else:
    print("Not Armstrong")