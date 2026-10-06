#import math
n =  int(input("Enter Any Number:"))
fact = 1
for i in range(n,0,-1):
    fact = fact*i
print("Factorial = ",fact)

#print("Factorial = ",math.factorial(n))
