'''21) Hollow Pyramid (Practice)
            *
           * *
          *   *
         *     *
        *********'''


num = int(input("Enter Number: "))

for i in range(1,num+1):

    #for spaces
    for spaces in range(1,num-i+1):
        print(" ",end="")

    #for star
    for star in range(1,i*2):
        if star==1 or star==i*2-1 or i==num:
            print("*",end="")
        else:
            print(" ",end="")
    print()