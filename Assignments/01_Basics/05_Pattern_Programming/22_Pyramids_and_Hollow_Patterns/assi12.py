'''12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1'''

n = int(input("Enter Number: "))
for i in range(1,n+1):
    print()
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1:
            print(i,end="")
        else:
            print(" ",end="")

for i in range(n-1,0,-1):
    print()
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1:
            print(i,end="")
        else:
            print(" ",end="")