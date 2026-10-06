'''Analyse and Print as per pattern
     *
    **
   ***
  ****
 *****
******'''

num = int(input("Enter Number = "))
i = 1

while i<=num:
    print()
    j=1
    while j<=num-i:
        print(" ",end="")
        j+=1
    star=1
    while star<=i:
        print("*",end="")
        star+=1   
    i+=1

