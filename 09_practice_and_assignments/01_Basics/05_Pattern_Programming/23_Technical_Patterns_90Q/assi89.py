'''89.
     1
    101
   10101
  1010101
 101010101   
10101010101'''

num = int(input("Enter Number: "))

for i in range(1,num+1):
    

    #for spaces
    for spaces in range(num-i,0,-1):
        print(" ",end="")

    #for numbers
    for numbers in range(1,i*2):
        if numbers%2==0:
            print("0",end="")
        else:
            print("1",end="")
    
    print()


