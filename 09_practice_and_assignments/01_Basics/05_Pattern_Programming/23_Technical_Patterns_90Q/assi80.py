'''80.
   *
  *_*
 *_*_*
*_*_*_*
 *_*_*
  *_*
   *  

   '''

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    #upper half
    for space in range(num-i,0,-1):
        print(" ",end="")
    for j in range(1,i*2):
        if j%2!=0:
           print("*",end="")
        else:
            print("_",end="")
for i in range(num-1,0,-1):
    print()
    #lower half
    for space in range(num-i,0,-1):
        print(" ",end="")
    for j in range(1,i*2):
        if j%2!=0:
           print("*",end="")
        else:
            print("_",end="") 