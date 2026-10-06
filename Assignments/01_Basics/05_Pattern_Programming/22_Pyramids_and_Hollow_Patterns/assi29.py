'''29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4'''

num = int(input("Enter Number: "))
count=1

for i in range(1,num+1):
    #for numbers
    for numbers in range(1,num+1):
        if i==numbers:
            print(i,end="")
        else:
            print("-",end="")
    print()