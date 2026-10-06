'''62.
    1
   123
  12345
 1234567
123456789
'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for star in range(1,2*i-1+1):
        print(star,end="")
    print()