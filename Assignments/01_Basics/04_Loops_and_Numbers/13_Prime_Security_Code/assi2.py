import math
num = int(input("Enter Number = "))
num = num+1


while True:
    flag=0
    i=2
    for i in range(i,int(math.sqrt(num))+1):
        if num%i==0:
            flag=1
            break
    if flag==0:
           print(num)
           break
    num+=1
 

