'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''

num = int(input("Enter Number = "))
sum = 0
product = 1

for i in str(num):
  sum+=int(i)
  product*=int(i)
  

if sum==product:
  print("Spy Number")
else:
  print("Not Spy Number")
