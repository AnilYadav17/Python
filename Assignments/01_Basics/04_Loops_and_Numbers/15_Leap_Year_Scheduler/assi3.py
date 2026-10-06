'''3.Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2'''

num1 = 0
num2 = 1
total = 0
count = 0


num = int(input("Enter Number of Months = "))
print("Population Growth = ")
for i in range(num):
  print(num1,end=" ")
  total+=num1
  if num1>5:
    count+=1
  num1,num2 = num2 , num1+num2
  
print("\nTotal Population =",total)
print("Months with Population > 5 =",count)

