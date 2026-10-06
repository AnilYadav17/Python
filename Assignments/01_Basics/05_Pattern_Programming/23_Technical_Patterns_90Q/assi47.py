'''47.
    1
   11
  1*1
 1**1
11111'''



num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        if i==num or k==1 or k==i:
            print("1",end="")
        else:
            print("*",end="")
    print()