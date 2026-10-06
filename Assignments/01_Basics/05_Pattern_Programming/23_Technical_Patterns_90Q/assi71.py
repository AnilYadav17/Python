'''71.
123456789
 1234567
  12345
   123
    1'''

num = int(input("Enter Number: "))
for i in range(1,num+1):

    #spaces
    for spaces in range(1,i):
        print(" ",end="")
    #numbers
    for star in range(1,num*2+2-i*2):
            print(star,end="")
    print()
