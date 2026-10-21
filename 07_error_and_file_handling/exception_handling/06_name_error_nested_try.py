try:
    print(x)
except NameError:
    print("Please check if variable exist")


try:
    import xyz
except ModuleNotFoundError:
    print("No module exist with this name.")

print("\n","-"*60,"\n")

import math
try:
    p = int(input("Enter Power: "))
    print(math.exp(10**p))
except OverflowError:
    print("Use small valuwe")



