'''2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N'''

import math
num = int(input("Enter Number = "))

i = 1
while i<=num:
    print("Number =", i,", Square =", i**2 ,", Cube =",i**3 ,", Square Root =",math.sqrt(i))
    i+=1