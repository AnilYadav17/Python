'''Analyse and Print as per pattern
 654321
  65432
   6543
    654
     65'''

num = int(input("Enter Number = "))
i = 1
while i<num:
    print()
    space=1
    while space<=i:
        print(" ",end="")
        space+=1
    j=num
    while j>=i:
        print(j,end="")
        j-=1
    i+=1

