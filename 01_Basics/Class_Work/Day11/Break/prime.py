n = int(input("Enter the Number = "))
if n<=1:
    print("Not Prime ")
else:
 x=0
 i=2
 while i<n:
     if n%i==0:
         x=1
         break
     i+=1
        
 if x==0: 
    print("Prime")
 else:
    print("Not Prime")
