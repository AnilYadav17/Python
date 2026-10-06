n1,n2 = map(int,input("Enter Both Numbers  = ").split())
if n1<n2:
   for i in range(n1,n2+1):
       if i%5==0 and i%10==5:
         print(i,end=" ")

elif n1>n2:
   for i in range(n2,n1+1):
       if i%5==0 and i%10==5:
         print(i,end=" ")

else:
   if n1%5==0:
     print("Same Number and Divisible by 5")
   else:
     print("Same Number and Not Divisible by 5")
