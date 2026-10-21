'''82.
   *
  *_* 
 *___* 
*_____*
 *___* 
  *_*
   *
   '''

num = int(input("Enter Number: "))


 #upper half
for i in range(1,num+1):
    print()
    for space in range(num-i,0,-1):
        print(" ",end="")
    for j in range(1,i*2):
        if j==1 or j==i*2-1:
            print("*",end="")
        else:
            print("_",end="")

 #lower half
for i in range(num-1,0,-1):
    print()
    #lower half
    for space in range(num-i,0,-1):
        print(" ",end="")
    for j in range(1,i*2):
        if j==1 or j==i*2-1 :
            print("*",end="")
        else:
            print("_",end="")