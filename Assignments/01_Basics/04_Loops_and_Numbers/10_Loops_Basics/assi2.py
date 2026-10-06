# 2. Factorial
n = int(input("n = "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Total Ways =", fact)
