n = int(input("Enter number = "))
p = len(str(n))
sum = 0
temp= n

while n>0:
    digit = n%10
    sum += digit**t
    n=n//10

if m==sum:
    print("Armstrong number ")
else:
    print("Not Armstrong")