
n = int(input("Enter Number = "))
sum = 0
m = n
while n>0:
  digit = n%10
  sum+=digit
  n= n//10

if m%sum==0:
 print("Harshad Number")
else:
 print("Not Harshad Number")
