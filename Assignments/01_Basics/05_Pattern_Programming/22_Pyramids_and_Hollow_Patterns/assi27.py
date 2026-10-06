'''27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10'''

num = int(input("Enter Number: "))
count=1

for i in range(1,num+1):
    
    #for spaces
    for spaces in range(num-1,i-1,-1):
        print(" ",end="")

    #for numbers
    for numbers in range(1,i):
        print(count,end=" ")
        count+=1
    print()