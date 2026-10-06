n = int(input("Enter any number :"))
sum = 0
m=n
while n>0:
    digit = n%10
    sum += digit**3
    n=n//10

if m==sum:
    print("Armstrong number ")
else:
    print("Not Armstrong")