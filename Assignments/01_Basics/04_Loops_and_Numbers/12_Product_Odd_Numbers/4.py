'''4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''

num = int(input("Enter Number = "))
n= num
sum = 0

'''while num>0:
   digit = num%10
   for i in range(digit,2,-1):
      factorial = factorial*i
   print(factorial)
   sum+=factorial
   num=num//10
if sum==n:
   print("Strong Number")
else:
   print("Not a Strong Number ")'''

while num>0:
  digit = num%10
  fact,i =1,1
  while i<=digit:
      fact *= i
      i+=1
  sum = sum+fact
  num = num//10
print("Sum",sum)
  
