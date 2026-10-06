'''6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29'''

num = int(input("Enter Number = "))

if num<2:
    print("Next Prime Cabin = 3")
else:
    num+=1
    while True:
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            print("Next Prime Cabin =",num)
            break
        num+=1