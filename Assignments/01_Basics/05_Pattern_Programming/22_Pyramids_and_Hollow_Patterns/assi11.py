'''11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1'''
num = int(input("Enter Number: "))
for i in range(1,num+1):
    print()
    #for first
    for first in range(1,num+1):
        if i>=first:
            print(first,end="")
    
    #for spaces
    for j in range((num-i)*2):
        print(" ",end="")

    #for second
    for k in range(i,0,-1):
        print(k,end="")



    
for i in range(num-1,0,-1):
    print()
    #for first
    for first in range(1,num+1):
        if i>=first:
            print(first,end="")
    
    #for spaces
    for j in range((num-i)*2):
        print(" ",end="")

    #for second
    for k in range(i,0,-1):
        print(k,end="")
