'''16) Palindrome Pyramid
            1
           121
          12321
         1234321
        123454321'''


num = int(input("Enter Number: "))

for i in range(1, num + 1):
    print()
    
    #for spaces
    for j in range(num, i, -1):
        print(" ", end="")
    
    #for numbers
    for k in range(1,i):
        print(k,end="")
    
    #for last numbers
    for l in range(i,0,-1):
        print(l,end="")