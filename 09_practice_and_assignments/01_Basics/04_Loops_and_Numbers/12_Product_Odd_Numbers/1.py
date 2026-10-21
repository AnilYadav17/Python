#while
'''n = int(input("Enter Number = "))
i=1
product = 1
while i<=n:
   if i%2==1:
      product = product*i
   i+=1
print("Product = ",product)'''


#for
n = int(input("Enter Number = "))
product = 1
for i in range(1,n+1,2):
    product *= i
print("Factorial = ",product)
