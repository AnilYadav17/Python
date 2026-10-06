'''84.
    1
   212
  32123
 4321234
543212345'''

num = int(input("Enter Number: "))

for i in range(1,num+1):

    #spaces
    for spaces in range(1,num-i+1):
        print(" ",end="")

    #left numbers
    for numbers in range(i,0,-1):
        print(numbers,end="")
   
    #right numbers
    for numbers in range(2,i+1):
        print(numbers,end="")
    
    print()