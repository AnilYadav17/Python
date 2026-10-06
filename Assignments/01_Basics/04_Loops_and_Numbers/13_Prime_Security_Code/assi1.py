import math
num = int(input("Enter Number = "))
if num<=1:
    print("Composite Number")
else:
    flag=0
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            flag=1
            break
    
    if flag==0:
        print("Prime Number")
    else:
        print("Composite Number")